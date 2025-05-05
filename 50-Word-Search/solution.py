# link: https://leetcode.com/problems/word-search/
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        
        def dfs(row, col, cache, w):
            if row >= m or col >= n or row < 0 or col < 0 or (row, col) in cache:
                return False
            if board[row][col] == w:
                return True
            if board[row][col] == w[0]:
                cache.add((row,col))
                new_cache = set(cache)
                val1 = dfs(row+1, col, new_cache, w[1:])
                new_cache = set(cache)
                val2 = dfs(row, col+1, new_cache, w[1:])
                new_cache = set(cache)
                val3 = dfs(row, col-1, new_cache, w[1:])
                new_cache = set(cache)
                val4 = dfs(row-1, col, new_cache, w[1:])
                
                return val1 or val2 or val3 or val4
            return False
            



        for x in range(len(board)):
            for y in range(len(board[0])):
                new_set = set()
                print("x, y first",x, y)
                value = dfs(x, y, new_set, word)
                if value:
                    return True

        return False