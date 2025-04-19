# link: https://leetcode.com/problems/maximum-star-sum-of-a-graph/description/
class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        graph = defaultdict(list)
        for start, end in edges:
            if vals[end] > 0:
                graph[start].append(vals[end])
            if vals[start] > 0:
                graph[end].append(vals[start])
        
        max_sum = -float('inf')
        for i in range(len(vals)):
            total = 0
            graph[i].sort(reverse=True)
            max_sum = max(max_sum, vals[i] + sum(graph[i][:min(len(graph[i]), k)]))
            
        return max_sum