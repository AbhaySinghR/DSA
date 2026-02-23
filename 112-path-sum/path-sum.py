# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        
        def psum(node,sum_t):

            if node is None:
                return False
            sum_t+=node.val
            
            if node.left==None and node.right==None:
                if sum_t==targetSum:
                    return True
                else:
                    return False

            l=psum(node.left,sum_t)
            r=psum(node.right,sum_t)
            return l or r
        
        return psum(root,0)