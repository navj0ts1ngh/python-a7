def odd_even(num: int) -> str:
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"


x = odd_even(3)
print(x)
