num = int(input("Enter a num: "))

result = 0

n = num
new = 0
digit = 0

while n > 0:
    digit = n % 10
    new = new * 10 + digit
    n //= 10

if new == num:
    print("Palindrome")
else:
    print("Not Palindrome")
