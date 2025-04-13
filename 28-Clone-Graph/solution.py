# link: https://leetcode.com/problems/clone-graph/
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        old_to_new = {} 

        def dfs(node):
            if node in old_to_new:
                return old_to_new[node]

            new_node = Node(node.val)
            old_to_new[node] = new_node
            
            for n in node.neighbors:
                new_node.neighbors.append(dfs(n)) 
            return new_node
        return dfs(node) if node else None

# time complexity: O(V + E)
# space complexity: O(V)
# V is the number of vertices (nodes) in the graph
# E is the number of edges in the graph
# The space complexity is O(V) because we are storing the mapping of old nodes to new nodes in a dictionary.