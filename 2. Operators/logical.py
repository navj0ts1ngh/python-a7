"""
Logical (AND, OR, NOT)

AND
C1  C2  Result
F   F   F
F   T   F
T   F   F
T   T   T

OR
C1  C2  Result
F   F   F
F   T   T
T   F   T
T   T   T

NOT (Reverse the result)
"""

physics = 54
chemistry = 10
# print(physics > 33 and chemistry > 33)
# print(physics > 33 or chemistry > 33)
# print(physics > 33 or chemistry > 33)
# print(not physics > 33)
# print(physics > 33 or not chemistry > 33)
print(not (not physics > 33 and not chemistry > 33))
