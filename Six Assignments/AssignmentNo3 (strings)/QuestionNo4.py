# 4. Write a Python program that accepts a string from user. Your program should create a new string in 
# reverse of first string and display it. 
# For example if the user enters the string 'EXAM' then new string would be 'MAXE' 

text = input("Enter a string: ")

my_reversed_text = text[::-1] # Reverse the string using slicing

print("New string in reverse order:" , my_reversed_text)
