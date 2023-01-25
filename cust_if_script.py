#!/usr/bin/env python3

grade = 'Your grade is '

percentage = float(input("What is your percentage score?"))

if percentage >= 90:
    grade = grade + 'A'
elif percentage >= 80:
    grade = grade + 'B'
elif percentage >= 70:
    grade = grade + 'C'
elif percentage >= 60:
    grade = grade + 'D'
else:
    grade = grade + 'F'
print (grade)


