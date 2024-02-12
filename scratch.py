"""

"""

import math

radius = int(input('please enter a radius: '))
print(type(radius))

circumference = 2 * math.pi * radius
print(circumference)

area = math.pi * radius ** 2

print(f'The circumference is {round(circumference)}, the area is {area} '
          f'for the radius {radius}')