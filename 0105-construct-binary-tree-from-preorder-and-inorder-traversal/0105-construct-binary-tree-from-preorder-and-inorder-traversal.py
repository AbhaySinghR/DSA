# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        hmap={}
        for i in range(len(inorder)):
            hmap[inorder[i]]=i
        
        self.pre_id=0
        
        def bt(left,right):

            if left>right:
                return None
            
            root_val=preorder[self.pre_id]
            self.pre_id+=1
            root=TreeNode(root_val)
            idx=hmap[root_val]

            root.left=bt(left,idx-1)
            root.right=bt(idx+1,right)
            return root

        return bt(0,len(inorder)-1)