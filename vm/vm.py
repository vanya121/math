import types
import dis
import builtins


class VirtualMachine:
    def __init__(self):
        self.stack = []

    def run(self, code: types.CodeType):
        a = list(dis.get_instructions(code))
        for item in a:
#            print(self.stack)
#            print(item)
            if item.opname == 'LOAD_NAME':
                self.stack.append(item.argval)
#            print(self.stack)
#            print(item)
            if item.opname == 'LOAD_CONST':
                self.stack.append(item.argval)
            if item.opname == 'CALL_FUNCTION':
                arg = self.stack.pop()
                func = self.stack.pop()
#                print(arg, func)
                f = builtins.__dict__[func](arg)
                self.stack.append(f)
#            print(self.stack)
#            print(item)
            if item.opname == 'POP_TOP':
                self.stack.pop()
            if item.opname == 'RETURN_VALUE':
                return 0
