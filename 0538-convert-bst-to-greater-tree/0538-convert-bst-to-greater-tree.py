# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        self.s=0
        def cbt(node):
            if node is None:
                return 
            
            cbt(node.right)
            self.s+=node.val
            node.val=self.s
            cbt(node.left)

        cbt(root)
        return root
        