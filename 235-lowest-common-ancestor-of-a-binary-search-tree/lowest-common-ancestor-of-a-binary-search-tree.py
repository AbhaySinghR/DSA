# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        self.lip=[]
        self.liq=[]
        def fp(node,li):
            if not node:
                return
            li.append(node)
            if node==p:
                self.lip=li.copy()
                return
            fp(node.left,li)
            fp(node.right,li)
            li.pop()
        
        fp(root,[])
        def fq(node,li):
            if not node:
                return
            li.append(node)
            if node==q:
                self.liq=li.copy()
                return
            fq(node.left,li)
            fq(node.right,li)
            li.pop()
        
        fq(root,[])

        if p in self.liq:
            return p
        if q in self.lip:
            return q
        res=None    
        for val in self.lip:
            if val in self.liq:
                res = val
        return res
        





        