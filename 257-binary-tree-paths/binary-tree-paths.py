# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        self.res=[]
        def fun(node,li):
            if not node:
                return
            li.append(node.val) 
            if node.left==None and node.right==None:
                self.res.append("->".join(map(str, li)))
            else:
                fun(node.left,li)
                fun(node.right,li)
            
            li.pop()

        fun(root,[])
        return self.res


        