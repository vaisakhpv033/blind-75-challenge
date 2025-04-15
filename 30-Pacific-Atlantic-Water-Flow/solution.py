# link: https://leetcode.com/problems/pacific-atlantic-water-flow/

from typing import List
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        row, col = len(heights), len(heights[0])
        pac, atla = set(), set() 

        def dfs(r, c, visited, prev_height):
            if (
                r < 0 or c < 0 
                or 
                r == row or c == col 
                or
                (r, c) in visited
                or 
                heights[r][c] < prev_height 
            ): return 

            visited.add((r, c))
            dfs(r-1, c, visited, heights[r][c])
            dfs(r+1, c, visited, heights[r][c])
            dfs(r, c-1, visited, heights[r][c])
            dfs(r, c+1, visited, heights[r][c])

        for c in range(col):
            dfs(0, c, pac, heights[0][c])
            dfs(row-1, c, atla, heights[row-1][c])

        for r in range(row):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, col-1, atla, heights[r][col-1])

        output = [] 
        for r in range(row):
            for c in range(col):
                if (r, c) in pac and (r, c) in atla:
                    output.append((r, c))
        return output
    
