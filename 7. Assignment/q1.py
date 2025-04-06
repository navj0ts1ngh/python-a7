# Factorial

num = int(input("Enter a num: "))

n = num
fact = 1

while num > 0:
    fact = fact * num
    num -= 1

print(fact)
