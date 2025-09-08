# Problem:
# Given an m*n matrix, if an element in the matrix is 0, 
# set its entire row and column to 0. Do this in place.

def setZeros(matrix):
    rows, cols = set(), set()
    m, n = len(matrix), len(matrix[0])

    # first pass: find positions of zeros
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                rows.add(i)
                cols.add(j)

    # second pass: set rows and cols to zero
    for i in range(m):
        for j in range(n):
            if i in rows or j in cols:
                matrix[i][j] = 0

    return matrix


# Example
mat = [[1, 1, 1],
       [1, 0, 1],
       [1, 1, 1]]

print(setZeros(mat))
