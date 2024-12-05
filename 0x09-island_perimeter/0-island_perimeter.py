#!/usr/bin/python3

# island_perimeter function

def island_perimeter(grid):
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    def dfs(r, c):
        if r < 0 or r >= rows or c < 0\
                or c >= cols or grid[r][c] == 0:
            return 1
        if grid[r][c] == 1:
            grid[r][c] = 2
            return dfs(r-1, c) + dfs(r+1, c)\
                + dfs(r, c-1) + dfs(r, c+1)
        return 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                perimeter += dfs(r, c)
    return perimeter
