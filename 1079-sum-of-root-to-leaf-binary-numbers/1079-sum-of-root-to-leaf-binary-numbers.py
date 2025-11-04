# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:

        self.fsum=0
        def fun(node,bin_s):
            if not node:
                return

            bin_s=bin_s+str(node.val)
            if node.left==None and node.right==None:
                num = int(bin_s, 2)
                self.fsum+=num
                return
            else:
                fun(node.left,bin_s)
                fun(node.right,bin_s)

        fun(root,'')
        return self.fsum

        