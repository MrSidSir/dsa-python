# Topic : Matrix Manipulation
# Real world use: Image rotation in photo editing apps, matrix operations in Machine Learning.

def rotate(matrix):
    n = len(matrix)

    # STEP 1: Transpose the matrix (swap rows with columns)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # STEP 2: Reverse each row (to get the rotated matrix)
    for row in matrix:
        row.reverse()


# Example input
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

rotate(matrix)
print(matrix)  # Output: [[7,4,1],[8,5,2],[9,6,3]]



#🔄 Workflow (Dry Run)

#Input:

#1 2 3
#4 5 6
#7 8 9


#Step 1 (Transpose): swap matrix[i][j] with matrix[j][i]

#1 4 7
#2 5 8
#3 6 9


#Step 2 (Reverse each row):

#7 4 1
#8 5 2
#9 6 3
