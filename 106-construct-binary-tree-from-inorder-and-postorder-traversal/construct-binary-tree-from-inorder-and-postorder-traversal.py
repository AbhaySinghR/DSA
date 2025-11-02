# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        hmap={}
        for i in range(len(inorder)):
            hmap[inorder[i]]=i
        
        self.post_id=len(postorder)-1

        def bt(left,right):
            if left>right:
                return None
            
            root_val=postorder[self.post_id]
            self.post_id-=1

            new_root=TreeNode(root_val)
            idx=hmap[root_val]

            new_root.right=bt(idx+1,right)
            new_root.left=bt(left,idx-1)
            

            return new_root
        return bt(0,len(inorder)-1)


