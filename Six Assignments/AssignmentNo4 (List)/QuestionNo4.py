# 4. Write a program that rotates the element of a list so that the element at the first index moves to the 
# second index, the element in the second index moves to the third index, etc., and the element in the last 
# index moves to the first index.  

user_input = input("Enter list elements..")

my_list = user_input.split()

if len(my_list) > 1:
    rotated_list = [my_list[-1]] + my_list[:-1]
else:
    rotated_list = my_list 

print("Rotated list:" , rotated_list)
