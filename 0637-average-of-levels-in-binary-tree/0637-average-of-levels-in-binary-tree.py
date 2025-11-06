# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        li=[]
        q=deque([root])
        while q:
            l_sum=0
            l_size=s=len(q)
            while l_size:
                node=q.popleft()
                l_sum+=node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                l_size-=1
            li.append(l_sum/s)
        return li
                
            




        