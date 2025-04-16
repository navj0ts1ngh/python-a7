mylist: list[int] = [1, 2, 3, 4, 5, 6]

# for element in mylist[::-1]:  # using indexing for list is not advisable
#     print(element)

# for i in range(len(mylist) - 1, -1, -1):
#     print(mylist[i])

i = len(mylist) - 1
while i > -1:
    print(mylist[i])
    i -= 1
