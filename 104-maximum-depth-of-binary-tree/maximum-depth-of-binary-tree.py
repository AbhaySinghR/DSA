# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def maxD(node):
            if node is None:
                return 0
            
            l=maxD(node.left)
            r=maxD(node.right)
            return 1 + max(l,r)

        return maxD(root)
        