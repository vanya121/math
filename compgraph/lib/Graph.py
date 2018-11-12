class Node(object):
    """
    class storing the current graph table
    """
    def __init__(self):
        self.data = []

    def create(self, input):
        """create table"""
        self.data = input

    def map(self, mapper):
        """
        generator that applies mapper to each row of the table
        """
        for item in self.data:
            yield from mapper(item)

    def reduce(self, tupal):
        """
        generator that applies a reducer to rows of a table with a key 'key'
        """
        key = tupal[0]
        reducer = tupal[1]
        from operator import itemgetter
        if self.data:
            prev_item_key = itemgetter(*key)(self.data[0])
            list_of_eq_key = []
            for item in self.data:
                if itemgetter(*key)(item) != prev_item_key:
                    yield from reducer(list_of_eq_key)
                    list_of_eq_key = []
                    prev_item_key = itemgetter(*key)(item)
                list_of_eq_key.append(item)
            yield from reducer(list_of_eq_key)

    def fold(self, tupal):
        """
        generator that sequentially calls the transmitted fold on
        the pair (state, new line) and returns the changed state
        """
        state = tupal[0]
        folder = tupal[1]
        for item in self.data:
            state = folder(state, item)
        yield state

    def sort(self, key):
        """
        sorts the table according to the key
        """
        from operator import itemgetter
        self.data.sort(key=itemgetter(*key))

    def join(self, tupal):
        """
        the operation of combining tables by key by one of the methods 'left', 'right', 'inner', 'outer'
        """
        keys = tupal[0]
        joined_g = tupal[1].node.data
        type = tupal[2]
        key_first = []
        key_second = []
        for i in range(len(keys) // 2):
            key_first.append(keys[i])
        for i in range(len(keys) // 2, len(keys)):
            key_second.append(keys[i])
        if keys:
            from operator import itemgetter
            self.data.sort(key=itemgetter(*key_first))
            joined_g.sort(key=itemgetter(*key_second))
        if type == 'outer':
            if len(keys) == 0:
                for item in self.data:
                    for it in joined_g:
                        yield from merg(item, it)
            else:
                yield from merg_outer(*keys, data_first=self.data, data_second=joined_g)
        if type == 'left':
            yield from merg_left(*keys, data_first=self.data, data_second=joined_g)
        if type == 'right':
            keys = keys[::-1]
            yield from merg_left(*keys, data_first=joined_g, data_second=self.data)
        if type == 'inner':
            yield from merg_inner(*keys, data_first=joined_g, data_second=self.data)


class Graph(object):
    """
    a class that stores a table and applies operations to it
    """
    def __init__(self):
        """node - table, functions - stores the names of the methods to be applied to the table,
        args - stores arguments for these functions, names - list of graphs and table names to be
        calculated before initializing the table of this graph, results - list of tables to specify
        the initial state of the table to be calculated before initialization of this table,
        generators - list of storing functions and their arguments until they are called,
        start - shows how to initialize a table, from an input table or other graph"""
        self.node = Node()
        self.functions = []
        self.args = []
        self.names = []
        self.result = []
        self.generators = []
        self.start = False

    def add_name(self, *name, **kwargs):
        """
        adds graph and table names and determines the start
        """
        for item in name:
            self.names.append(item)
        if kwargs:
            self.start = kwargs['start']

    def add_map(self, mapper):
        """
        adds a map operation on the table
        """
        self.functions.append('map')
        self.args.append(mapper)

    def add_sort(self, key):
        """
         adds a sort operation on the table
         """
        self.functions.append('sort')
        self.args.append(key)

    def add_reduce(self, key, reducer):
        """
        adds a reduce operation on the table
        """
        self.functions.append('reduce')
        self.args.append((key, reducer))

    def add_fold(self, state, folder):
        """
        adds a fold operation on the table
        """
        self.functions.append('fold')
        self.args.append((state, folder))

    def add_join(self, key, joined_g, type):
        """
        adds a join operation on the table
        """
        self.functions.append('join')
        self.args.append((key, joined_g, type))

    def run(self, **kwargs):
        """
        starts the calculation of the table
        """
        for item in self.names:
            if type(item) == Graph:
                self.result.append(item.run(**kwargs))
        if self.start:
            if kwargs:
                self.node.create(kwargs[self.names[0]])
            else:
                self.node.create(self.result[0])
        else:
            if not self.result:
                self.node.create(kwargs[self.names[0]])
            else:
                self.node.create(self.result[0])
        for func, arg in zip(self.functions, self.args):
            if func == 'sort':
                for generator in self.generators:
                    self.node.data = list(getattr(self.node, generator[0])(generator[1]))
                getattr(self.node, func)(arg)
                self.generators.clear()
            else:
                self.generators.append((func, arg))
        for generator in self.generators:
            self.node.data = list(getattr(self.node, generator[0])(generator[1]))
        return self.node.data


def merg_left(*keys, data_first, data_second):
    """
    generator for operations 'left join' and 'right join'
    """
    key_first = []
    key_second = []
    for i in range(len(keys) // 2):
        key_first.append(keys[i])
    for i in range(len(keys) // 2, len(keys)):
        key_second.append(keys[i])
    from operator import itemgetter
    i = 0
    j = 0
    null_dict = {}
    if data_second:
        for key in data_second[0]:
            null_dict[key] = None
    while i < len(data_first):
        if j >= len(data_second):
            while i < len(data_first):
                yield from merg(data_first[i], null_dict)
                i += 1
        else:
            if itemgetter(*key_first)(data_first[i]) == itemgetter(*key_second)(data_second[j]):
                j_ = j
                while j_ < len(data_second) and itemgetter(*key_first)(data_first[i]) == itemgetter(*key_second)(data_second[j_]):
                    yield from merg(data_first[i], data_second[j_])
                    j_ += 1
                i += 1
            elif itemgetter(*key_first)(data_first[i]) < itemgetter(*key_second)(data_second[j]):
                yield from merg(data_first[i], null_dict)
                i += 1
            else:
                j += 1


def merg_outer(*keys, data_first, data_second):
    """
    generator for oreration outer join
    """
    key_first = []
    key_second = []
    for i in range(len(keys) // 2):
        key_first.append(keys[i])
    for i in range(len(keys) // 2, len(keys)):
        key_second.append(keys[i])
    from operator import itemgetter
    i = 0
    j = 0
    null_dict_second = {}
    for key in data_second[0]:
        null_dict_second[key] = None
    null_dict_first = {}
    for key in data_first[0]:
        null_dict_first[key] = None
    while i < len(data_first):
        if j >= len(data_second):
            while i < len(data_first):
                yield from merg(data_first[i], null_dict_second)
                i += 1
        else:
            if itemgetter(*key_first)(data_first[i]) == itemgetter(*key_second)(data_second[j]):
                j_ = j
                while j_ < len(data_second) and itemgetter(*key_first)(data_first[i])\
                        == itemgetter(*key_second)(data_second[j_]):
                    yield from merg(data_first[i], data_second[j_])
                    j_ += 1
                i += 1
                j += 1
            elif itemgetter(*key_first)(data_first[i]) < itemgetter(*key_second)(data_second[j]):
                yield from merg(data_first[i], null_dict_second)
                i += 1
            else:
                yield from merg(null_dict_first, data_second[j])
                j += 1
    while j < len(data_second):
        yield from merg(null_dict_first, data_second[j])
        j += 1


def merg_inner(*keys, data_first, data_second):
    """
    generator for oreration inner join
    """
    key_first = []
    key_second = []
    for i in range(len(keys) // 2):
        key_first.append(keys[i])
    for i in range(len(keys) // 2, len(keys)):
        key_second.append(keys[i])
    from operator import itemgetter
    i = 0
    j = 0
    while i < len(data_first) and j < len(data_second):
        if itemgetter(*key_first)(data_first[i]) == itemgetter(*key_second)(data_second[j]):
            j_ = j
            while j_ < len(data_second) and itemgetter(*key_first)(data_first[i])\
                    == itemgetter(*key_second)(data_second[j_]):
                yield from merg(data_first[i], data_second[j_])
                j_ += 1
            i += 1
        elif itemgetter(*key_first)(data_first[i]) < itemgetter(*key_second)(data_second[j]):
            i += 1
        else:
            j += 1


def merg(first, second):
    """
    join table rows
    """
    new_dict = {}
    for key in first:
        new_dict[key] = first[key]
    for key in second:
        new_dict[key] = second[key]
    yield new_dict
