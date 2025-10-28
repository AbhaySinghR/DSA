# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        if p==None and q==None:
            return True
        
        q1=deque([p])
        q2=deque([q])
        while q1 and q2:
            curr1=q1.pop()
            curr2=q2.pop()
            if curr1 and curr2:
                if curr1.val!=curr2.val:
                    return False
            else:
                return False

            if curr1.left or curr2.left:
                q1.append(curr1.left)
                q2.append(curr2.left)

            if curr1.right or curr2.right:
                q1.append(curr1.right)
                q2.append(curr2.right)
        
        return True

        