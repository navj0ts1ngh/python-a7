# Lambda functions = Anonymous, i.e. they dont have a name
# Use only when your function contains one liners


def odd_even(num: int) -> bool:
    return num % 2 == 0


func = lambda num: num % 2 == 0
print(func(10))
print(func(11))


def total_marks(phy, chem, eng):
    return phy + chem + eng


total_marks = lambda phy, chem, eng: phy + chem + eng
print(total_marks(10, 20, 30))
