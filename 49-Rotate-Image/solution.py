# link: https://leetcode.com/problems/rotate-image/
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        cache = {}
        n = len(matrix)
        for x in range(n):
            for y in range(n):
                new_x, new_y = y, n - 1 - x
                cache[(new_x, new_y)] = matrix[new_x][new_y]
                if (x,y) in cache:
                    matrix[new_x][new_y] = cache[(x,y)]
                else:
                    matrix[new_x][new_y] = matrix[x][y]

# time complexity: O(n^2)
# space complexity: O(n^2)