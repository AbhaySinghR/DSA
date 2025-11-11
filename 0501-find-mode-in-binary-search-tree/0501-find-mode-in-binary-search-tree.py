# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:

        self.hmap={}
        def fMode(node):
            if not node:
                return 
            
            self.hmap[node.val]=self.hmap.get(node.val,0)+1
            fMode(node.left)
            fMode(node.right)
        
        fMode(root)
        a=max(self.hmap.values())
        li=[]
        for i,j in self.hmap.items():
            if j==a:
                li.append(i)
        
        return li

        