# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root==None:
            return 0
        d=1
        max_d=0
        stack=[(root,d)]
        while stack:
            curr,d=stack.pop()
            max_d=max(d,max_d)
            if curr.left:
                stack.append((curr.left,d+1))
            if curr.right:
                stack.append((curr.right,d+1))
        
        return max_d
        