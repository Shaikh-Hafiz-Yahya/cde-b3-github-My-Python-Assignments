# 5. Write a program that prompts the user to enter a number n, and then prints all the 
# odd numbers between 1 and n.  

n = int(input("Enter a number: "))

for i in range(1, n+1, 2):
    print(i)
