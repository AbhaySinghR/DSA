# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':


        li_p=[]
        li_q=[]
        curr=root
        while curr:
            li_p.append(curr)
            if p.val==curr.val:
                break
            elif p.val>curr.val:
                curr=curr.right
            else:
                curr=curr.left

        curr=root
        while curr:
            li_q.append(curr)
            if q.val==curr.val:
                break
            elif q.val>curr.val:
                curr=curr.right
            else:
                curr=curr.left

        if p in li_q:
            return p
        if q in li_p:
            return q
        res=None
        for i in li_p:
            if i in li_q:
                res=i
        return res


       