# Methods -> Functions
# They are bound to a specific object/class

my_list = [4, 5, 2, 1, 5, 1, 34, 1, "Nav"]

my_list.append(10)
my_list.append(100)
my_list.append(20)

my_list.insert(3, 999)
x = my_list.pop()
print(x)

del my_list[3]

my_list.remove(1)

my_list.append([1, 2, 3, 4])

my_list.extend([1, 2, 3])

print(my_list)


del my_list
