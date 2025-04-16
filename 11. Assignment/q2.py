def simple_calculator(num1: float, num2: float, operator: str) -> float | str:
    if ord(operator) == 43:
        return num1 + num2
    elif ord(operator) == 45:
        return num1 - num2
    return "Error"


print(simple_calculator(2.1, 3.4, "."))
