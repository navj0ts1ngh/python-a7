num = int(input("Enter a number:"))

if num % 2 == 0 and num > 0:
    print("positive and even")
elif num % 2 != 0 and num > 0:
    print("positive and odd")
elif num % 2 == 0 and num < 0:
    print("negative and even")
elif num % 2 != 0 and num < 0:
    print("negative and odd")
else:
    print("zero")
