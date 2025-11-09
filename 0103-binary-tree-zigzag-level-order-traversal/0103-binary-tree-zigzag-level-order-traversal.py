# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []
        lvl=0
        li=[]
        q=deque([root])
        while q:
            n_li=[]
            s=len(q)
            while s:
                node=q.popleft()
                n_li.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                s-=1
            if lvl%2==0:
                li.append(n_li)
            else:
                li.append(n_li[:][::-1])
            
            lvl+=1
        
        return li
            




        