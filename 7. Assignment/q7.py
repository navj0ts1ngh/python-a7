num = int(input("Enter a num: "))


while num >= 10:
    sum = 0
    while num > 0:
        sum += num % 10
        num //= 10
    num = sum
print(num)
