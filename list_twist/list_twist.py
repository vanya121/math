from collections import UserList


class ListTwist(UserList):
    aliases1 = {
        'first': 'F',
        'another': 'F',
        }
    aliases = {
        'last': 'L',
        'another': 'L',
        }
    aliases2 = {
        'size': 'S',
        'another': 'S',
        }

    def __init__(self, data=[]):
        super().__init__(data)

    def __len__(self):
        return len(self.data)

    def __setattr__(self, attr, value):
        if attr == 'data':
            self.__dict__[attr] = value
        if attr == 'last' or attr == 'L':
            if not self.data:
                raise NotImplementedError
            attr = self.aliases.get(attr, attr)
            UserList.__setattr__(self, attr, value)
            self.__dict__['last'] = value
            self.__dict__['data'].pop()
            self.__dict__['data'].append(value)
        if attr == 'first' or attr == 'F':
            if not self.data:
                raise NotImplementedError
            attr = self.aliases1.get(attr, attr)
            UserList.__setattr__(self, attr, value)
            self.__dict__['first'] = value
            self.__dict__['data'].pop(0)
            self.__dict__['data'].insert(0, value)
        if attr == 'size' or attr == 'S':
            if value < 0:
                raise NotImplementedError
            elif value == 0:
                self.__dict__['data'].clear()
                self.__dict__['last'] = None
                self.__dict__['first'] = None
            else:
                attr = self.aliases2.get(attr, attr)
                UserList.__setattr__(self, attr, value)
                if value < len(self.__dict__['data']):
                    while value < len(self.__dict__['data']):
                        self.__dict__['data'].pop()
                if value > len(self.__dict__['data']):
                    while value > len(self.__dict__['data']):
                        self.__dict__['data'].append(None)
                self.__dict__['last'] = (self.__dict__['data'])[len(self.data) - 1]
                self.__dict__['first'] = (self.__dict__['data'])[0]

    def __getattr__(self, attr):
        if attr == 'first' or attr == 'F':
            if len(self.data) == 0:
                raise NotImplementedError
            else:
                self.first = self.data[0]
                return self.first
        if attr == 'last' or attr == 'L':
            if len(self.data) == 0:
                raise NotImplementedError
            else:
                self.last = self.data[len(self.data) - 1]
                return self.last
        if attr == 'reversed' or attr == 'R':
            if not self.data:
                raise NotImplementedError
            return self.data[::-1]
        if attr == 'last' or attr == 'L':
            if not self.data:
                raise NotImplementedError
            return self.data[len(self.data) - 1]
        if attr == 'size' or attr == 'S':
            return len(self.data)
