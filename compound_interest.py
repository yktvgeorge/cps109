"""
this program will create a compound interest calculator
"""
import math


principal = int(input('Enter the principal amount: '))
rate = float(input('Enter the savings rate (.05 for 5%): '))
year = int(input('Enter the number of years to save: '))

amount = principal * (1 + rate) ** year

print(amount)



