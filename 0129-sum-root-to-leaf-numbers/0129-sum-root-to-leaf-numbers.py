# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        self.final_sum=0
        def rsum(node,s):

            if not node:
                return 
            s+=str(node.val)
            if node.left == None and node.right == None:
                self.final_sum+=int(s)
            else:
                rsum(node.left, s)
                rsum(node.right,s)
            

        rsum(root,'')
        return self.final_sum

        