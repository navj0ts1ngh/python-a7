# def largest(num1: int = None, num2: int = None, num3: int = None) -> int:
#     if num1 != None and num2 != None and num3 != None:
#         if num1 > num2 and num1 > num3:
#             return num1
#         elif num2 > num1 and num2 > num3:
#             return num2
#         return num3
#     return -1


# With Annotations another way
# int | None --- It means it can be an int or None
def largest_part2(
    num1: int | None = None, num2: int | None = None, num3: int | None = None
) -> int:
    if num1 != None and num2 != None and num3 != None:
        if num1 > num2 and num1 > num3:
            return num1
        elif num2 > num1 and num2 > num3:
            return num2
        else:
            return num3
    else:
        return -1


print(
    largest_part2(
        1,
        2,
    )
)

# we can also wite defalut as num1: int = 0
