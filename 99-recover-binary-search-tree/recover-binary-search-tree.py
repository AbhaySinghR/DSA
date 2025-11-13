# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        

        self.w1=None
        self.w2=None
        self.prev=TreeNode(float('-inf'))
        
        def inord(node):
            if not node:
                return

            inord(node.left)
            if node.val < self.prev.val:
                if not self.w1:
                    self.w1=self.prev
                self.w2=node

            self.prev=node

            inord(node.right)
        
        inord(root)

        self.w1.val,self.w2.val=self.w2.val,self.w1.val
