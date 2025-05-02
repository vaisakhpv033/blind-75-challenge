# link: https://leetcode.com/problems/set-matrix-zeroes/
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        row, col = 0, 0
        zero_row, zero_col = set(), set()
        m, n = len(matrix), len(matrix[0])
        while row < m:
            col = 0
            while col < n:
                print(row, col, matrix[row][col])
                if matrix[row][col] == 0:
                    zero_row.add(row)
                    zero_col.add(col)
                col += 1
            row += 1
        
        for row in zero_row:
            for col in range(len(matrix[0])):
                matrix[row][col] = 0

        for row in range(len(matrix)):
            for col in zero_col:
                matrix[row][col] = 0

        
# time complexity: O(mn)
# space complexity: O(m+n)