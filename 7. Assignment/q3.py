num = int(input("Enter a num: "))

count = 0

for i in range(1, int(num**0.5) + 1):
    if num % i == 0:
        count += 1
        if num // i != i:
            count += 1

print(count)
