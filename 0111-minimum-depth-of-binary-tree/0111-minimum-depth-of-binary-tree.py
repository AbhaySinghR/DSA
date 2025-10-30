# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:

        def min_height(node):
            if not node:
                return 0
            
            left_height=min_height(node.left)
            right_height=min_height(node.right)
            
            if node.left and node.right:
                height=1+min(left_height,right_height)
            else:
                height=1+max(left_height,right_height)

            return height
        return min_height(root)



        