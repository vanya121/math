class Case:
    def __init__(self, name: str, text_code: str):
        self.name = name
        self.text_code = text_code


TEST_CASES = [
    Case(
        name="constant",
        text_code=r"""
print(17)
"""),
    Case(
        name="bbb",
        text_code=r"""
a = 1
b = 2
print(a + b)
"""),
    Case(
        name="bbb2",
        text_code=r"""
a = 1
b = 2
print(a * b)
"""),
    Case(
        name="bbb3",
        text_code=r"""
a = 2
b = 3
print(a ** b)
"""),
    Case(
        name="const2",
        text_code=r"""
print(2 ** 3)
"""),
    Case(
        name="test102",
        text_code=r"""
d = {1: 2, 3: 4}
print(d[1])
"""),
    Case(
        name="test61",
        text_code=r"""
class T(object):
    def __init__(self):
        self._a = 1

t = T()
print(t._a)
"""),
    Case(
        name="catching_IndexError",
        text_code=r"""
try:
    [][1]
    print("Shouldn't be here...")
except IndexError:
    print("caught it!")
""")
]
