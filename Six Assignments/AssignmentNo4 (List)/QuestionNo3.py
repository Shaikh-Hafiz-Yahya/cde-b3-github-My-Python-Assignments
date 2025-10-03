# 3. Find and display the largest number of a list without using built-in function max(). Your program 
# should ask the user to input values in list from keyboard. 

user_input = input("Enter numbers separated by space: ")

my_list = [int(x) for x in user_input.split()]

largest = my_list[0]

for num in my_list[1:]:
    if num > largest:
        largest = num

print("The largest number is " , largest)
