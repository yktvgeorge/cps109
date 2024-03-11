"""
this program determines if an aurline passenger is eligible
for a 25% discount

Discount applies if passenger is either 6 or less years old
or 65 or older
"""

# Prompt for the passenger name
# Prompt for the passenger age
# Print if the passenger is eligible for the discount

name = input('Enter passenger name: ')
age = int(input('Enter passenger age: '))

if age <=6 or age >= 65
    print(f'{name} is eligible for the discount!')
else:
    print(f'{name} is not eligible for the discount')