"""
Pass by value (Immutable)
int, str, float, tuple

Pass by reference (Mutable)
list, set, dict
"""


def change(a):
    # local variable
    a = 100


def change2(b, a):
    print(f"address of b inside {id(b)}")
    a = 1000
    b.append(10)
    print(f"address of b inside {id(b)}")


b = [1, 2, 3, 4, 5]
a = 5
print(f"address of b inside {id(b)}")
change2(b, a)
change(a)
print(a)
print(b)
