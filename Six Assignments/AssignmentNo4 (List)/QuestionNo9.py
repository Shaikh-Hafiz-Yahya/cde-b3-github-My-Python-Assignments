# 9. Write a program to add two matrices of size n x m.

m = int(input("Enter number of rows: "))
n = int(input("Enter number of columns: "))

print("Enter first matrix:")
A = [list(map(int, input().split())) for _ in range(m)]

print("Enter second matrix:")
B = [list(map(int, input().split())) for _ in range(m)]

C = [[A[i][j] + B[i][j] for j in range(n)] for i in range(m)]

print("Resultant Matrix after Addition:")

for row in C:
    print(row)



