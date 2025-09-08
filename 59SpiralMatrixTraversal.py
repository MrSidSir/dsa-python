def spiralorder(matrix):
    res = []  # yahan result list banayi jisme spiral traversal ka order store hoga

    if not matrix:  # agar matrix empty hai to empty list return kar do
        return res

    # boundaries set karte hain
    top, bottom = 0, len(matrix)          # top = first row, bottom = last row index + 1
    left, right = 0, len(matrix[0])       # left = first column, right = last column index + 1

    # jab tak boundaries valid hain
    while top < bottom and left < right:

        # STEP 1: Traverse Right → (left se right tak upar wali row me)
        for i in range(left, right):
            res.append(matrix[top][i])
        top += 1   # upar wali row traverse ho gayi, ab next row se start karenge

        # STEP 2: Traverse Down → (top se bottom tak rightmost column me)
        for i in range(top, bottom):
            res.append(matrix[i][right-1])
        right -= 1  # rightmost column ho gaya, ab ek column andar aa jao

        # agar ab boundaries cross kar gayi to loop tod do
        if not (top < bottom and left < right):
            break

        # STEP 3: Traverse Left → (right-1 se left tak neeche wali row me)
        for i in range(right-1, left-1, -1):
            res.append(matrix[bottom-1][i])
        bottom -= 1  # neeche wali row traverse ho gayi, ab ek row upar aa jao

        # STEP 4: Traverse Up → (bottom-1 se top tak leftmost column me)
        for i in range(bottom-1, top-1, -1):
            res.append(matrix[i][left])
        left += 1  # leftmost column ho gaya, ab ek column andar aa jao

    return res  # final result return kar do


# Test Example
print(spiralorder([[1,2,3],[4,5,6],[7,8,9]]))
# Output: [1,2,3,6,9,8,7,4,5]
