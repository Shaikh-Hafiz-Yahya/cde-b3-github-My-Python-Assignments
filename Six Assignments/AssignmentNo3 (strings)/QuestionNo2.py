# 2. Write a program that reads a string from keyboard and display: 
# * The number of uppercase letters in the string 
# * The number of lowercase letters in the string 
# * The number of digits in the string 
# * The number of whitespace characters in the string  

text_from_user = input("Enter a string: ")

upper_count = 0
lower_count = 0
digit_count = 0
space_count = 0

for char in text_from_user:

    if char.isupper():
        upper_count += 1

    elif char.islower():
        lower_count += 1

    elif char.isdigit():
        digit_count += 1

    elif char.isspace():
        space_count += 1

print("Number of uppercase letters:", upper_count)
print("Number of lowercase letters:", lower_count)
print("Number of digits:", digit_count)
print("Number of whitespace characters:", space_count)
