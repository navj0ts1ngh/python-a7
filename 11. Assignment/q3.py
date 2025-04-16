def check_number(num: int) -> str:
    if num == 0:
        return "zero"
    elif num > 0:
        return "positive"
    return "negative"


print(check_number(0))
