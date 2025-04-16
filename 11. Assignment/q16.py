def largest(mylist: list[int]) -> int:
    largest = mylist[0]

    for i in mylist:
        if i > largest:
            largest = i

    return largest


mylist = [1, 59, 17, 2, 3, 4, 555, 6, 10]
print(largest(mylist))
