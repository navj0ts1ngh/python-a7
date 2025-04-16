# indexing/positions

my_list: list[int | float | str] = [1, 2, 3, 44.5, 5, 6, 7, 8, 9, 10, 11, 12, 113]
print(my_list[0])
print(my_list[1])
print(my_list[2])

# #list index out of range
# print(my_list[66])

n = len(my_list)
print(n)
print(my_list[n - 1])

# #index out of range
# print(my_list[n])
