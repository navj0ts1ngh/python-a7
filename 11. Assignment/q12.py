mylist: list[int | float] = [10, 20, 30, 3, 6, 9, 25, 6]

count = 0
for i in mylist:
    if i % 5 == 0:
        count += 1

print(f"Numbers divisible by 5 are:{count}")
