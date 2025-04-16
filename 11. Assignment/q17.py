def smallest(mylist: list[int]) -> int:
    smallest = mylist[0]

    for i in mylist:
        if i < smallest:
            smallest = i

    return smallest


mylist = [1, 59, 17, 2, -3, 4, 555, 6, 10]
print(smallest(mylist))
