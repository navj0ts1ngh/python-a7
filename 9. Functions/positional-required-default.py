def calculate(physics, chemistry, hindi=0, english=0, computer=0):
    print(f"physics = {physics}")
    print(f"chemistry = {chemistry}")
    print(f"hindi = {hindi}")
    print(f"english = {english}")
    print(f"computer = {computer}")

    total = physics + chemistry + hindi + english + computer
    print(f"Your total marks = {total}")


calculate(10, 20)
calculate(
    4,
    5,
    6,
    7,
)
print()

# Named arguments
calculate(1, 2, 3, 4, 5)
calculate(english=10, hindi=19, physics=20, chemistry=10, computer=43)
calculate(45, 17, english=10, hindi=19, computer=43)
