# 12. write a program that takes a positive integer N as input and calculates the sum of 
# the reciprocals of all numbers from 1 up to N. The program should display the final sum.

n = int(input("Enter a +ive integer N.. "))
total = 0

for i in range(1 , n+1):
    total += 1/i
print("Sum of reciprocal is = ", total)
