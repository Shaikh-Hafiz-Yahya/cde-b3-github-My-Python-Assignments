# 6. Write a program that asks the user to input his name and print its initials. Assuming that the user 
# always types first name, middle name and last name and does not include any unnecessary spaces. 
# For example, if the user enters Ajay Kumar Garg the program should display A. K. G. 
# Note:Don't use split() method 

name = input("Enter your full name...")

initials = ""

initials += name[0].upper() + ". "

for i in range(1, len(name)):
    if name[i-1] == " ":   # character after space
        initials += name[i].upper() + ". "

print("Initials::", initials.strip())
