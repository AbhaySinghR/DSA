# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:




        if root is None:
            return False
        def pt(node,s):

            if node is None:
                return False
            s+=node.val
            if node.left is None and node.right is None:
                if s==targetSum:
                    return True
                else:
                    return False
            
            l=pt(node.left,s)
            r=pt(node.right,s)
            return l or r
        
        return pt(root,0)
        