# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def pathsum(node,csum):
            if not node:
                return False
            csum+=node.val
            if node.left == None and node.right==None:
                if csum==targetSum:
                    return True
            
            left_s=pathsum(node.left,csum)
            right_s=pathsum(node.right,csum)
            return left_s or right_s
        return pathsum(root,0)