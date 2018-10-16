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

            if item.opname == 'NOP':
                pass

            if item.opname == 'POP_TOP':
                self.stack.pop()

            if item.opname == 'ROT_TWO':
                a = self.stack.pop()
                b = self.stack.pop()
                self.stack.append(a)
                self.stack.append(b)

            if item.opname == 'ROT_THREE':
                a = self.stack.pop()
                b = self.stack.pop()
                c = self.stack.pop()
                self.stack.append(a)
                self.stack.append(c)
                self.stack.append(b)

            if item.opname == 'DUP_TOP':
                a = self.stack.pop()
                self.stack.append(a)
                self.stack.append(a)

            if item.opname == 'DUP_TOP_TWO':
                a = self.stack.pop()
                self.stack.append(a)
                self.stack.append(a)

            if item.opname == 'UNARY_POSITIVE':
                TOS = self.stack.pop()
                TOS = +TOS
                self.stack.append(TOS)

            if item.opname == 'UNARY_NEGATIVE':
                TOS = self.stack.pop()
                TOS = -TOS
                self.stack.append(TOS)

            if item.opname == 'UNARY_NOT':
                TOS = self.stack.pop()
                TOS = not TOS
                self.stack.append(TOS)

            if item.opname == 'UNARY_INVERT':
                TOS = self.stack.pop()
                TOS = ~TOS
                self.stack.append(TOS)

            if item.opname == 'GET_ITER':
                TOS = self.stack.pop()
                TOS = iter(TOS)
                self.stack.append(TOS)

            if item.opname == 'BINARY_ADD' or item.opname == 'INPLACE_ADD':
                TOS = self.dic[self.stack.pop()]
                TOS1 = self.dic[self.stack.pop()]
                self.stack.append(TOS + TOS1)

            if item.opname == 'BINARY_FLOOR_DIVIDE' or item.opname == 'INPLACE_FLOOR_DIVIDE':
                TOS = self.dic[self.stack.pop()]
                TOS1 = self.dic[self.stack.pop()]
                self.stack.append(TOS1 // TOS)

            if item.opname == 'BINARY_LSHIFT' or item.opname == 'INPLACE_LSHIFT':
                TOS = self.dic[self.stack.pop()]
                TOS1 = self.dic[self.stack.pop()]
                self.stack.append(TOS1 << TOS)

            if item.opname == 'BINARY_AND' or item.opname == 'INPLACE_AND':
                TOS = self.dic[self.stack.pop()]
                TOS1 = self.dic[self.stack.pop()]
                self.stack.append(TOS1 & TOS)

            if item.opname == 'BINARY_MODULO' or item.opname == 'INPLACE_MODULO':
                TOS = self.dic[self.stack.pop()]
                TOS1 = self.dic[self.stack.pop()]
                self.stack.append(TOS1 % TOS)

            if item.opname == 'BINARY_MULTIPLY' or item.opname == 'INPLACE_MULTIPLY':
                TOS = self.dic[self.stack.pop()]
                TOS1 = self.dic[self.stack.pop()]
                self.stack.append(TOS1 * TOS)

            if item.opname == 'BINARY_OR' or item.opname == 'INPLACE_OR':
                TOS = self.dic[self.stack.pop()]
                TOS1 = self.dic[self.stack.pop()]
                self.stack.append(TOS1 | TOS)

            if item.opname == 'BINARY_POWER' or item.opname == 'INPLACE_POWER':
                TOS = self.dic[self.stack.pop()]
                TOS1 = self.dic[self.stack.pop()]
                self.stack.append(TOS1 ** TOS)

            if item.opname == 'BINARY_RSHIFT' or item.opname == 'INPLACE_RSHIFT':
                TOS = self.dic[self.stack.pop()]
                TOS1 = self.dic[self.stack.pop()]
                self.stack.append(TOS1 >> TOS)

            if item.opname == 'BINARY_MATRIX_MULTIPLY' or item.opname == 'INPLACE_MATRIX_MULTIPLY':
                TOS = self.dic[self.stack.pop()]
                TOS1 = self.dic[self.stack.pop()]
                self.stack.append(TOS1 @ TOS)

            if item.opname == 'BINARY_SUBTRACT' or item.opname == 'INPLACE_SUBTRACT':
                TOS = self.dic[self.stack.pop()]
                TOS1 = self.dic[self.stack.pop()]
                self.stack.append(TOS1 - TOS)

            if item.opname == 'BINARY_TRUE_DIVIDE' or item.opname == 'INPLACE_TRUE_DIVIDE':
                TOS = self.dic[self.stack.pop()]
                TOS1 = self.dic[self.stack.pop()]
                self.stack.append(TOS1 / TOS)

            if item.opname == 'BINARY_XOR' or item.opname == 'INPLACE_XOR':
                TOS = self.dic[self.stack.pop()]
                TOS1 = self.dic[self.stack.pop()]
                self.stack.append(TOS1 ^ TOS)

            if item.opname == 'BINARY_SUBSCR':
                TOS = self.dic[self.stack.pop()]
                TOS1 = self.dic[self.stack.pop()]
                self.stack.append(TOS1[TOS])

            if item.opname == 'COMPARE_OP':
                a = self.stack.pop()
                if a in self.dic:
                    a = self.dic[a]
                b = self.stack.pop()
                if b in self.dic:
                    b = self.dic[b]
                if item.argval == '>':
                    self.stack.append(a < b)
                if item.argval == '<':
                    self.stack.append(a > b)
                if item.argval == '==':
                    self.stack.append(a == b)
                if item.argval == '!=':
                    self.stack.append(a != b)
                if item.argval == '<=':
                    self.stack.append(a >= b)
                if item.argval == '>=':
                    self.stack.append(a <= b)
            if item.opname == 'POP_JUMP_IF_FALSE':
                pass

            if item.opname == 'CALL_FUNCTION':
                z = self.stack.pop()
                if z in self.dic:
                    arg = self.dic[z]
                else:
                    arg = z
                func = self.stack.pop()
                f = builtins.__dict__[func](arg)
                self.stack.append(f)

            if item.opname == 'RETURN_VALUE':
                return self.stack.pop()
