# 10. Write a program to multiply two matrices 

m = int(input("Rows of A: "))
n = int(input("Columns of A ( and rows of B ): "))
p = int(input("Columns of B: "))

print("Enter first matrix A:")

A = [list(map(int, input().split())) for _ in range(m)]

print("Enter second matrix B:")

B = [list(map(int, input().split())) for _ in range(n)]

C = [[sum(A[i][k] * B[k][j] for k in range(n)) for j in range(p)] for i in range(m)]

print("Result:")

for r in C:
    print(*r)
