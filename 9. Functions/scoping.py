def change():
    a = 100
    b = 105
    print("Inside function")
    print(f"id(a)->{id(a)}, id(b)->{id(b)}")
    print(a)
    print(b)


def change2():
    # don't use global variables as a general practice
    global a, b
    print("Inside function 2")
    print(f"id(a)->{id(a)}, id(b)->{id(b)}")
    a = 100
    b = 105
    print(a)
    print(b)


a = 5
b = 15
print("Outside function")
print(f"id(a)->{id(a)}, id(b)->{id(b)}")
change()
change2()
print("--------")
print(a)
print(b)
print("Outside function after changing values inside change2 function")
print(f"id(a)->{id(a)}, id(b)->{id(b)}")
