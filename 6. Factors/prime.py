import sys

num = int(input("Enter a num: "))

n = num
count = 0

for i in range(2, int(num**0.5) + 1):
    if num % i == 0:
        print("Not Prime")
        sys.exit()
print("Prime")
