# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        dummy=TreeNode(0)
        self.curr=dummy
        def fun(node):
            if not node:
                return 
            
            self.curr.right = node
            self.curr = node
            left = node.left
            right = node.right
            node.left=None
            node.right=None
            fun(left)
            fun(right)
        fun(root)
        
        return dummy.right