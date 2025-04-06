num = int(input("Enter a num: "))

n = num
sum = 0

for i in range(1, int(num**0.5) + 1):
    if num % i == 0:
        sum += i
        if num // i != i and num // i != num:
            sum += num // i

if sum == num:
    print("True")
else:
    print("False")
