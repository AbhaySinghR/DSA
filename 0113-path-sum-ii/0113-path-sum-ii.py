# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        self.targetSum=targetSum
        self.final_li=[]
        def psum(node,fsum,li):
            if not node:
                return 
            
            fsum+=node.val
            li.append(node.val)
            if node.left==None and node.right==None:
                if fsum>self.targetSum:
                    return 
                if fsum==self.targetSum:
                    self.final_li.append(li)
            else:
                psum(node.left,fsum,li.copy())
                psum(node.right,fsum,li.copy())

        psum(root,0,[])
        return self.final_li
        