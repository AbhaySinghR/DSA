# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:

        def cnt_node(node):
            if not node:
                return 0
            
            l=cnt_node(node.left)
            r=cnt_node(node.right)
            n=1+l+r
            return n

        return cnt_node(root)

        