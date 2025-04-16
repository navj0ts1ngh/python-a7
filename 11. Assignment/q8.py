def middle(num1: int, num2: int, num3: int) -> int:
    if (num1 <= num2 <= num3) or (num3 <= num2 <= num1):
        return num2
    elif (num2 <= num1 <= num3) or (num2 <= num1 <= num3):
        return num1
    return num3


def divisible(num: int) -> str:
    if num % 3 == 0 and num % 4 == 0:
        return "divisible"
    return "not divisible"


print(divisible(middle(3, 2, 30)))
