# List/Array

# this works in every version of python
from typing import List

my_list: list[int | float | str] = [1, 2, 3, 44.5, "abc", True]
print(my_list)
print(type(my_list))

your_list: List[int | float | str] = [1, 2, 3, 44.5, "abc", True]
print(your_list)
