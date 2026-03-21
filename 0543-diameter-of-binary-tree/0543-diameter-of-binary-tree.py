# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        self.d=float('-inf')
        def diam(node,d):
            if node is None:
                return 0
            
            l=diam(node.left,self.d)
            r=diam(node.right,self.d)
            h=max(l,r)+1
            self.d=max(self.d,l+r)
            return h
        res=diam(root,self.d)
        return self.d


        