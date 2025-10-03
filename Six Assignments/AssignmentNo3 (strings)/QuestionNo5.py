# 5. Write a Python program that accepts a string from user. Your program should create a new string by 
# shifting one position to left. 
# For example if the user enters the string 'examination 2021' then new string would be 'xamination 
# 2021e'   

text = input("Enter a string..")

if len(text) > 1:
    new_text = text[1:] + text[0]
else:
    new_text = text  

print("New string after shifting left:" , new_text)
