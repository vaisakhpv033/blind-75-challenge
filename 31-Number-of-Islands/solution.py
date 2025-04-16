# link: https://leetcode.com/problems/number-of-islands/
from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        visited = set() 

        island_count = 0

        def bfs(r, c):
            if (
                r < 0 or c < 0
                or
                r >= rows or c >= cols
                or 
                (r, c) in visited
                or 
                grid[r][c] == "0"
            ): return 
            visited.add((r, c))
            bfs(r-1, c)
            bfs(r+1, c)
            bfs(r, c-1)
            bfs(r, c+1)
            return

        for r in range(rows):
            for c in range(cols):
                if ((r,c) not in visited and grid[r][c] != "0"):
                    bfs(r, c)
                    island_count += 1

        return island_count
    
# time complexity: O(m*n) where m is the number of rows and n is the number of columns in the grid.
# space complexity: O(m*n) for the visited set in the worst case where all cells are land.