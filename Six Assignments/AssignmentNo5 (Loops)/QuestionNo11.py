# 11. Write a program that asks the user for a positive integer value. The program should 
# calculate the sum of all the integers from 1 up to the number entered. For example, if 
# the user enters 20, the loop will find the sum of 1, 2, 3, 4, ... 20.  

n = int(input("Enter a positive integer::"))
total = 0

for i in range(1 , n + 1):

    total += i

print("Sum = " , total)
