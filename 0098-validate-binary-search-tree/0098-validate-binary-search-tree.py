# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        self.li=[]
        def inord(node):
            if not node:
                return 
            
            inord(node.left)
            self.li.append(node.val)
            inord(node.right)
        inord(root) 
        
        for i in range(len(self.li)-1):
            if self.li[i]>=self.li[i+1]:
                return False
        
        return True


        
        