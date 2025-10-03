# 8. Write a program that prompts the user to input a number and prints its multiplication 
# table. 

n = int(input("Enter a number: "))
print(f"Multiply table of {n} :")

for i in range(1 , 11):
    print(f"{n} x {i} = {n * i}")
