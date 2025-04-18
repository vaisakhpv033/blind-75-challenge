# link: https://leetcode.com/problems/find-building-where-alice-and-bob-can-meet/
class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        
        res = [-1 for i in range(len(queries))]

        groups = defaultdict(list)

        for idx, query in enumerate(queries):
            query.sort()
            left, right = query

            max_heig = max(heights[left], heights[right])

            if left==right or heights[left] < heights[right]:
                res[idx] = right
            else:
                h = max(heights[left], heights[right])
                groups[right].append((h, idx))
            
        min_heap = [] 
        for idx, h in enumerate(heights):
            for query_height, query_idx in groups[idx]:
                heapq.heappush(min_heap, (query_height, query_idx))
            
            while min_heap and h > min_heap[0][0]:
                query_height, query_idx = heapq.heappop(min_heap)
                res[query_idx] = idx

        return res
                

# time Complexity: O(NLogN+QLogN)
# space Complexity: O(N)