# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:

        def minD(node):

            if node is None:
                return 0
            
            l=minD(node.left)
            r=minD(node.right)
            
            if l==0:
                return 1 + r
            if r==0:
                return 1 + l 
            
            return 1 + min(l,r)
            
        return minD(root)



        