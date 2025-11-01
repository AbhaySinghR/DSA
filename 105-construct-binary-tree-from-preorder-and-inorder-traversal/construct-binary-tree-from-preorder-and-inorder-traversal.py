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
        
        self.pre_idx=0

        def bt(left,right):

            if left>right:
                return None

            new_root=preorder[self.pre_idx]
            self.pre_idx+=1

            root=TreeNode(new_root)

            split_idx=hmap[new_root]

            root.left=bt(left,split_idx-1)
            root.right=bt(split_idx+1,right)

            return root
        
        return bt(0,len(inorder)-1)


            