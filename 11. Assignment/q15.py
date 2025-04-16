def sumOddEven(mylist: list[int]):
    sum_odd = 0
    sum_even = 0
    for i in mylist:
        if i % 2 == 0:
            sum_even += i
        else:
            sum_odd += i
    print(f"sum of odd numbers are {sum_odd}")

    print(f"sum of even numbers are {sum_even}")


mylist: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
sumOddEven(mylist)
