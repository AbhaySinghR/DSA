# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        self.cnt=0
        self.targetSum=targetSum
        self.hmap={
                    0:1
                   }

        def psum(node,fsum):
            if not node:
                return
            fsum+=node.val
            n=fsum-self.targetSum
            if n in self.hmap:
                self.cnt+=self.hmap[n]
            self.hmap[fsum]=self.hmap.get(fsum,0)+1
            psum(node.left,fsum)
            psum(node.right,fsum)
            self.hmap[fsum] -= 1
        
        psum(root,0)
        return self.cnt
        