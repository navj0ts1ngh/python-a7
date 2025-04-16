my_list: list[int | float | str] = [1, 2, 3, 44.5, 5, 6, 7, 8, 9, 10, 11, 12, 113]

n = len(my_list)

# iterate by index
for i in range(0, n):
    print(my_list[i], end=" ")

for i in range(12, -1, -1):
    print(my_list[i], end=" ")

# Iterate by value

print()
for num in my_list:
    print(num, end=" ")


print()
for i in my_list:
    print(id(i), end=" ")

print("----------------------------")

for i in range(0, n):
    print(id(my_list[i]), end=" ")


# reversing using iteration by value, its has timecomplexity O(2n)
for num in my_list[::-1]:
    print(num, end=" ") 
