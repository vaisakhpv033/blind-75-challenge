# link: https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/description/

class UnionFind:

    def __init__(self, n):
        self.parent = [i  for i in range(n)] 

        self.size = [1 for _ in range(n)]

    def find(self, x): 

        if x == self.parent[x]: 
            return x 
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    
    def union(self, u,v): 
        root1 = self.find(u)
        root2 = self.find(v)

        if root1 != root2: 
            if self.size[root1] > self.size[root2]: 
                self.parent[root2] = root1 
                self.size[root1] += 1 
            else: 
                self.parent[root1] = root2 
                self.size[root2]  += 1 


class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:


        uf = UnionFind(n)
        for u, v in edges: 
            uf.union(u,v)

        
        for i in range(n): 
            uf.parent[i] = uf.find(i)

        count = Counter(uf.parent)
        lengths = count.values()

     
        answer = (n*(n-1))//2 
        for length in lengths: 
            answer -= (length*(length-1))//2 

        return answer