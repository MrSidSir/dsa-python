def spiralorder(matrix):
    res = []
    if not matrix: 
        return res

    top, bottom = 0, len(matrix)
    left, right = 0, len(matrix[0])

    while top < bottom and left < right:
        # traverse right
        for i in range(left, right):
            res.append(matrix[top][i])
        top += 1

        # traverse down
        for i in range(top, bottom):
            res.append(matrix[i][right-1])
        right -= 1

        if not (top < bottom and left < right):
            break

        # traverse left
        for i in range(right-1, left-1, -1):
            res.append(matrix[bottom-1][i])
        bottom -= 1

        # traverse up
        for i in range(bottom-1, top-1, -1):
            res.append(matrix[i][left])
        left += 1

    return res

print(spiralorder([[1,2,3],[4,5,6],[7,8,9]]))
# Output: [1,2,3,6,9,8,7,4,5]
