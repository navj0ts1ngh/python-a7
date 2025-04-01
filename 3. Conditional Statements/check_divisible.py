"""
num
num divisible by 3 -> FOO
num divisible by 5 -> BAR
num divisible by 3and5 -> FOOBAR
else -> FOOFOOBARBAR
"""

n = int(input("Enter number"))

if n % 3 == 0 or n % 5 == 0:
    print()
