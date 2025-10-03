# 3. Write a Python program that accepts a string from user. Your program should create and display a
# new string where the first and last characters have been exchanged. 

text = input("Enter a string: ")

if len(text) > 1:
    new_text = text[-1] + text[1:-1] + text[0]
else:
    new_text = text  

print("New string after swapping first & last characters:" , new_text)

