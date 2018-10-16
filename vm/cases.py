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
        name="1",
        text_code=r"""
a = 1
b = 2
print(a + b)
"""),
    Case(
        name="2",
        text_code=r"""
a = 1
b = 2
print(a * b)
"""),
    Case(
        name="3",
        text_code=r"""
a = 2
b = 3
print(a ** b)
"""),
    Case(
        name="4",
        text_code=r"""
a = 2
print(a ** 2)
"""),

    Case(
        name="5",
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
        name="test1024",
        text_code=r"""
d = 9
d *= 3
print(d)
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
"""),
    Case(
        name="QWERR2",
        text_code=r"""
print(3 > 2)
"""),
    Case(
        name="12",
        text_code=r"""
a = 1
a = a + 1
print(a)
"""),
    Case(
        name="13",
        text_code=r"""
a = 1
a += 1
print(a)
"""),
    Case(
        name="14",
        text_code=r"""
a = 1
if a > 0:
    print(a)
"""),
    Case(
        name="15",
        text_code=r"""
a = 1
if a > 2:
    print(1)
else:
    print(0)
"""),
    Case(
        name="16",
        text_code=r"""
a = 10
if a > 2:
    print(1)
else:
    print(0)
"""),
    Case(
        name="17",
        text_code=r"""
a = 3
while a == 3:
    a += 1
"""),
    Case(
        name="18",
        text_code=r"""
a = [1, 2, 3]
print(a[0])
"""),
    Case(
        name="19",
        text_code=r"""
a = (1, 2, 3)
print(a[0])
"""),
Case(
        name="21",
        text_code=r"""
a = {'a', 2, 'c'}
print('c' in a)
"""),
Case(
    name="22",
    text_code=r"""
print(1 & 0)
"""),
Case(
    name="23",
    text_code=r"""
for i in range(2):
    print(i)
""")
]
