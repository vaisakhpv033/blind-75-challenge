# link: https://leetcode.com/problems/unique-paths/
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = {}
        def paths(row, col):
            if row == 1 and col == 1:
                return 1
            elif row == 0:
                return 0
            elif col == 0:
                return 0

            if (row, col) in cache:
                return cache[(row, col)]

            top = paths(row-1, col)
            left = paths(row, col-1)

            cache[(row, col)] = top + left
            return cache[(row, col)]
            
        return paths(m, n)
    
# time complexity: O(m*n)
# space complexity: O(m*n)
# m is the number of rows and n is the number of columns