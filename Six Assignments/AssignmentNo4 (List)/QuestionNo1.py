#                                List Assignment:
# 1. Write a program that accepts a list from user and print the alternate element of list. 

user_input = input("Enter list elements separated_by_space:")

my_list = user_input.split()

print("Alternate elements of the list::")

for i in range(0 , len(my_list) , 2):
    print(my_list[i])
