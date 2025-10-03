# 8. Find the sum of each row of matrix of size m x n. For example for the following matrix output will be 
# like this : 
# Sum of row 1 = 32 
# Sum of row 2 = 31 
# Sum of row 3 = 63 

rows = int(input("Enter number of rows: "))
n = int(input("Enter number of columns: "))

matrix = []
print("Enter matrix elements row by row:")
for i in range(rows):
    row = list(map(int , input().split()))
    matrix.append(row)

for i in range(rows):
    row_sum = sum(matrix[i])
    print(f"Sum of row {i+1} = {row_sum}")
