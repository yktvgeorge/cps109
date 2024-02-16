"""
i will be creating a program that will
find the maximum and minimum from a list
"""


numbers: list[int] = [10, 8, 15, 3, 13, 17]
type(numbers)

max(numbers)
min(numbers)

def min_max(list):
    return min(list), max(list)

print(max(numbers))
print(min(numbers))



