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

    def __init__(self, data=[]):
        super().__init__(data)

    def __len__(self):
        return len(self.data)

    def __setattr__(self, attr, value):
        if attr == 'data':
            self.__dict__[attr] = value
        if attr == 'last' or attr == 'L':
            if not self.data:
                raise AttributeError
            attr = self.aliases.get(attr, attr)
            UserList.__setattr__(self, attr, value)
            self.__dict__['last'] = value
            self.__dict__['data'].pop()
            self.__dict__['data'].append(value)
        if attr == 'first' or attr == 'F':
            if not self.data:
                raise AttributeError
            attr = self.aliases1.get(attr, attr)
            UserList.__setattr__(self, attr, value)
            self.__dict__['first'] = value
            self.__dict__['data'].pop(0)
            self.__dict__['data'].insert(0, value)

    def __getattr__(self, attr):
        if attr == 'reversed' or attr == 'R':
            if not self.data:
                raise AttributeError
            return self.data[::-1]
        if attr == 'last' or attr == 'L':
            if not self.data:
                raise AttributeError    
            return self.data[len(self.data) - 1]
        if attr == 'size' or attr == 'S':
            return len(self.data)
