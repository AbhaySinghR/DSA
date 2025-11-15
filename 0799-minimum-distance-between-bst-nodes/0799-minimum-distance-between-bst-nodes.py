
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:

        self.li=[]
        min_diff=float('inf')
        def inord(node):

            if not node:
                return 
            
            inord(node.left)
            self.li.append(node.val)
            inord(node.right)
        
        inord(root)
        for i in range(len(self.li)-1):
            min_diff=min(min_diff, abs(self.li[i]-self.li[i+1]))
        
        return min_diff


            
        