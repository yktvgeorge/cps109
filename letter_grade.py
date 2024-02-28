"""
In this program you will enter a numeric number that will determine
your grade at North Shore Community College
"""

grade = (input('Enter a numeric grade: '))

if grade < 60:
    grade = 'F'
    print('Your grade is a', grade)

if 60 <= grade and grade <= 62:
    grade = 'D-'
    print('Your grade is a', grade)

if 63 <= grade and grade <= 66:
    grade = 'D'
    print('Your grade is a', grade)

if 67 <= grade and grade <= 69:
    grade = 'D+'
    print('Your grade is a', grade)

if 70 <= grade and grade <= 72:
    grade = 'C-'
    print('Your grade is a', grade)

if 73 <= grade and grade <= 76:
    grade = 'C'
    print('Your grade is a', grade)

if 77 <= grade and grade <= 79:
    grade = 'C+'
    print('Your grade is a', grade)

if 80 <= grade and grade <= 82:
    grade = 'B-'
    print('Your grade is a', grade)

if 83 <= grade and grade <= 86:
    grade = 'B'
    print('Your grade is a', grade)

if 87 <= grade and grade <= 89:
    grade = 'B+'
    print('Your grade is a', grade)

if 90 <= grade and grade <= 92:
    grade = 'A-'
    print('Your grade is a', grade)

if 93 <= grade and grade <= 100:
    grade = 'A'
    print('Your grade is a', grade)



