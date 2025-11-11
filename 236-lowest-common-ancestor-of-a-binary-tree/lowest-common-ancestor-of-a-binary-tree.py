# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        self.pli=[]
        self.qli=[]
        def lca_p(node,li):
            if not node:
                return 
            li.append(node)
            if node==p:
                self.pli=li.copy()
                return
            
            lca_p(node.left,li)
            lca_p(node.right,li)
            li.pop()

        def lca_q(node,li):
            if not node:
                return 
            li.append(node)
            if node==q:
                self.qli=li.copy()
                return
            
            lca_q(node.left,li)
            lca_q(node.right,li)
            li.pop()
        
        lca_p(root,[])    
        lca_q(root,[])

        if p in self.qli:
            return p
        if q in self.pli:
            return q
        
        res = None
        for val in self.pli:
            if val in self.qli:
                res = val
        return res
        
        
        