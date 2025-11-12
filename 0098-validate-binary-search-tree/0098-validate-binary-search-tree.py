# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        self.prev=None
        self.flag=True
        
        def inord(node):
            if not node or not self.flag:
                return
            
            inord(node.left)

            if self.prev is not None and node.val<=self.prev:
                self.flag=False
                return 
            
            self.prev=node.val

            inord(node.right)
        
        inord(root)
        return self.flag

        
        