# A school has following rules for grading system:

# a. Below 25 - F

# b. 25 to 45 - E

# c. 45 to 50 - D

# d. 50 to 60 - C

# e. 60 to 80 - B

# f. Above 80 - A

# Ask user to enter marks and print the corresponding grade.


marks_user = int(input("Enter your marks:"))

if marks_user < 25:
    grade = "F"
elif marks_user <= 45:
    grade = "E"
elif marks_user <= 50:
    grade = "D"
elif marks_user <= 60:
    grade = "C"
elif marks_user <= 80:
    grade = "B"
else:
    grade = "A"

print(f"Your grade is: {grade}") #f 'string method {}..' 
