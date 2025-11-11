# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.li=[]
        def ksmall(node):

            if not node:
                return 
            
            ksmall(node.left)
            self.li.append(node.val)
            ksmall(node.right)

        ksmall(root)
        return self.li[k-1]
        
            
        