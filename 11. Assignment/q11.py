mylist: list[int | float] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 24, 36]

# # by value
# for i in mylist:
#     if i % 3 == 0 and i % 4 == 0:
#         print(i, end=" ")

# By index
for i in range(0, len(mylist)):
    if mylist[i] % 3 == 0 and mylist[i] % 4 == 0:
        print(mylist[i], end=" ")
