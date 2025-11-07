# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:


        if not root:
            return []
        final_li=[]
        q=deque([root])
        while q:
            li=[]
            size_q=len(q)
            while size_q:
                node=q.popleft()
                li.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                size_q-=1
            
            final_li.append(li)
        
        return final_li

        