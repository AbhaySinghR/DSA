# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def bal(node):
            if not node:
                return 0, True
        
            left_height, left_balanced = bal(node.left)
            right_height, right_balanced = bal(node.right)

            balance=(
                left_balanced and right_balanced and abs(left_height-right_height)<=1
                )
            height = 1 + max(left_height,right_height)
            return height, balance

        return bal(root)[1]

        