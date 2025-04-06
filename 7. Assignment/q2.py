num = int(input("Enter a num: "))

for i in range(1, int(num**0.5) + 1):
    if num % i == 0:
        print(i)
        if num // i != i:
            print(num // i)
