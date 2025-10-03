# Strings Assignments:-
# 1. Write a program that accepts a string from user. Your program should count 
# and display number of vowels in that string. 

text = input("Enter a string: ")

vowels = "aeiouAEIOU"

count = 0

for char in text:
    if char in vowels:  #nested if
        count += 1 #Augment statement += 

print(f"Number of vowels in the string:: {count}")
