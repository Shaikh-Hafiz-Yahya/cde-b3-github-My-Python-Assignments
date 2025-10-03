# 10. Write a Python program to print the first 6 terms of a geometric sequence starting 
# with 2 and having a common ratio of 3. 
# The program should output the following sequence: 
# 2 6 18 54 162 486  

a = 2     
r = 3    

for i in range(6):
    print(a * (r ** i), end = " ")
