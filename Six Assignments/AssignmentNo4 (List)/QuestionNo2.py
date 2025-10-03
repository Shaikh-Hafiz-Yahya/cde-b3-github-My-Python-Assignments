# 2. Write a program that accepts a list from user. Your program should reverse the content of list and 
# display it. Do not use reverse() method.  

user_input = input("Enter list elements::")

my_list = user_input.split()

reversed_list = []

for i in range(len(my_list) - 1, -1, -1):
    reversed_list.append(my_list[i])

print("Reversed list::" , reversed_list)
