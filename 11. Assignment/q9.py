def average(num1: float, num2: float, num3: float) -> float:
    return (num1 + num2 + num3) / 3


def check_average(result: float, num4: float) -> int:
    if result > num4:
        return 1
    elif result == num4:
        return 0
    return -1


num1 = float(input("Enter first number:"))
num2 = float(input("Enter second number:"))
num3 = float(input("Enter third number:"))
num4 = float(input("Enter fourth number:"))

output = check_average(average(num1, num2, num3), num4)
if output == 1:
    print(f"average of {num1},{num2},{num3} numbers is greater than {num4}")
elif output == 0:
    print(f"average of {num1},{num2},{num3} numbers is equal than {num4}")
else:
    print(f"average of {num1},{num2},{num3} numbers is less than {num4}")
