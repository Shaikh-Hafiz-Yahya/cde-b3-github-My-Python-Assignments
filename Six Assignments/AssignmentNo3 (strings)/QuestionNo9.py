# 9. Write a program in python that accepts a string to setup a passwords. Your entered password must 
# meet the following requirements: 
# The password must be at least eight characters long. 
# It must contain at least one uppercase letter. 
# It must contain at least one lowercase letter. 
# It must contain at least one numeric digit. 
# Your program should should perform this validation.  

password = input("Set your password...")

has_upper = False
has_lower = False
has_digit = False

for char in password:
    if char.isupper():
        has_upper = True
    elif char.islower():
        has_lower = True
    elif char.isdigit():
        has_digit = True

if (len(password) >= 8 and has_upper and has_lower and has_digit):
    print("Password is valid")

else:
    print("Password is invalid")
    print("Requirements:")
    print(" At least 8 characters long")
    print(" At least one uppercase letter")
    print(" At least one lowercase letter")
    print(" At least one numeric digit")
