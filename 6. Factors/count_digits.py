num = int(input("Enter a num: "))

n = num
count = 0

while n > 0:
    count += 1
    n //= 10

print(count)
