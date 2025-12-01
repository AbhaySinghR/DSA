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

        hmap={}

        def dfs(node):

            if node not in hmap:
                new=Node(node.val)
                hmap[node]=new
                for n in node.neighbors:
                    new.neighbors.append(dfs(n))
                return new
            else:
                return hmap[node]

        return dfs(node) if node else None

        
        