def exist(board, word):
    rows, cols = len(board), len(board[0])
    path = set()

    def dfs(r, c, i):
        if i == len(word): return True
        if (r < 0 or c < 0 or r >= rows or c >= cols or 
            word[i] != board[r][c] or (r, c) in path):
            return False
        
        path.add((r, c))
        res = (dfs(r+1, c, i+1) or dfs(r-1, c, i+1) or 
               dfs(r, c+1, i+1) or dfs(r, c-1, i+1))
        path.remove((r, c))  # Fixed: remove tuple, not separate args
        return res
    
    for r in range(rows):
        for c in range(cols):
            if dfs(r, c, 0): 
                return True
    return False  # Fixed: moved outside the loop

# Example
board = [["A","B","C","E"],
         ["S","F","C","S"], 
         ["A","D","E","E"]]

print(exist(board, "ABCCED"))  # True
print(exist(board, "SEE"))     # True  
print(exist(board, "ABCB"))    # False