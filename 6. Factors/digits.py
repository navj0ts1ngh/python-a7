"""
Extraction of digits
"""

num = int(input("Enter a num: "))
digit = 0

while num != 0:
    digit = num % 10
    print(digit, end=" ")
    num //= 10
