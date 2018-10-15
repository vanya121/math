import types
import dis
import builtins


class VirtualMachine:
    def __init__(self):
        self.stack = []
        self.dic = {}

    def run(self, code: types.CodeType):
        a = list(dis.get_instructions(code))
        for item in a:
#            print(self.stack)
#            print(self.dic)
#            print(item)
            if item.opname == 'LOAD_NAME':
                self.stack.append(item.argval)

            if item.opname == 'STORE_NAME':
                tmp = self.stack.pop()
                self.dic[item.argval] = tmp

            if item.opname == 'LOAD_CONST':
                if item.argval is not None:
                    self.dic[item.argval] = item.argval
                self.stack.append(item.argval)

            if item.opname == 'BINARY_ADD':
                TOS = self.dic[self.stack.pop()]
                TOS1 = self.dic[self.stack.pop()]
                self.stack.append(TOS + TOS1)

            if item.opname == 'BINARY_FLOOR_DIVIDE':
                TOS = self.dic[self.stack.pop()]
                TOS1 = self.dic[self.stack.pop()]
                self.stack.append(TOS1 // TOS)

            if item.opname == 'BINARY_LSHIFT':
                TOS = self.dic[self.stack.pop()]
                TOS1 = self.dic[self.stack.pop()]
                self.stack.append(TOS1 << TOS)

            if item.opname == 'BINARY_AND':
                TOS = self.dic[self.stack.pop()]
                TOS1 = self.dic[self.stack.pop()]
                self.stack.append(TOS1 & TOS)

            if item.opname == 'BINARY_MODULO':
                TOS = self.dic[self.stack.pop()]
                TOS1 = self.dic[self.stack.pop()]
                self.stack.append(TOS1 % TOS)

            if item.opname == 'BINARY_MULTIPLY':
                TOS = self.dic[self.stack.pop()]
                TOS1 = self.dic[self.stack.pop()]
                self.stack.append(TOS1 * TOS)

            if item.opname == 'BINARY_OR':
                TOS = self.dic[self.stack.pop()]
                TOS1 = self.dic[self.stack.pop()]
                self.stack.append(TOS1 | TOS)

            if item.opname == 'BINARY_POWER':
                TOS = self.dic[self.stack.pop()]
                TOS1 = self.dic[self.stack.pop()]
                self.stack.append(TOS1 ** TOS)

            if item.opname == 'BINARY_RSHIFT':
                TOS = self.dic[self.stack.pop()]
                TOS1 = self.dic[self.stack.pop()]
                self.stack.append(TOS1 >> TOS)

            if item.opname == 'BINARY_RSHIFT':
                TOS = self.dic[self.stack.pop()]
                TOS1 = self.dic[self.stack.pop()]
                self.stack.append(TOS1 >> TOS)

            if item.opname == 'BINARY_SUBTRACT':
                TOS = self.dic[self.stack.pop()]
                TOS1 = self.dic[self.stack.pop()]
                self.stack.append(TOS1 - TOS)

            if item.opname == 'BINARY_TRUE_DIVIDE':
                TOS = self.dic[self.stack.pop()]
                TOS1 = self.dic[self.stack.pop()]
                self.stack.append(TOS1 / TOS)

            if item.opname == 'BINARY_XOR':
                TOS = self.dic[self.stack.pop()]
                TOS1 = self.dic[self.stack.pop()]
                self.stack.append(TOS1 ^ TOS)

            if item.opname == 'CALL_FUNCTION':
                arg = self.stack.pop()
                func = self.stack.pop()
                f = builtins.__dict__[func](arg)
                self.stack.append(f)

            if item.opname == 'POP_TOP':
                self.stack.pop()

            if item.opname == 'RETURN_VALUE':
                return self.stack.pop()
