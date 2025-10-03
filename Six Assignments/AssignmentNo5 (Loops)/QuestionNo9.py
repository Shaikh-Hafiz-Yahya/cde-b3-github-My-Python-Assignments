# 9. Write a Python program to print the first 8 terms of an arithmetic progression starting 
# with 3 and having a common difference of 4. 
# The program should output the following sequence: 
# 3 7 11 15 19 23 27 31 

a = 3    
d = 4     

for i in range(8):
    print(a + i * d , end = " ")
