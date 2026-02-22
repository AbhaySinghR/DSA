# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def symm(n1,n2):

            if n1==None and n2==None:
                return True
            if n1==None or n2==None:
                return False
            
            if n1.val!=n2.val:
                return False
            
            a=symm(n1.left,n2.right)
            b=symm(n1.right,n2.left)

            return a and b
        
        return symm(root, root)