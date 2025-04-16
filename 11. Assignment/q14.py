def countOddEven(mylist: list):
    count_odd = 0
    count_even = 0
    for i in mylist:
        if i % 2 == 0:
            count_even += 1
        else:
            count_odd += 1
    print(f"count of odd numbers are {count_odd}")

    print(f"count of even numbers are {count_even}")


mylist: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
countOddEven(mylist)
