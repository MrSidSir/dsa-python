# 58 number of islands (DFS or BFS) 
# Topic :- Grapg Traversal(DFS/BFS)
# Real world use:- image segmentation, landmass detection in satellite maps
def numIslands(grid):
    def dfs(r, c):
        if (r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] == '0'):
            return
        grid[r][c] = '0'
        dfs(r+1, c)
        dfs(r-1, c)
        dfs(r, c+1)
        dfs(r, c-1)

    count = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == '1':
                dfs(r, c)
                count += 1
    return count


grid = [
    ["1","1","0","0"],
    ["1","0","0","1"],
    ["0","0","1","1"],
    ["0","0","0","1"]
]

print(numIslands(grid))   # Expected output: 3

