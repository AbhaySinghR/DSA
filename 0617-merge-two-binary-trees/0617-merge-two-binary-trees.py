# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:

        def fun(node1,node2):
            if not node1 and not node2:
                return None
            if not node1 and node2:
                root=TreeNode(node2.val)
            elif not node2 and node1:
                root=TreeNode(node1.val)
            else:
                root=TreeNode(node1.val+node2.val)

            left1 = node1.left if node1 else None
            left2 = node2.left if node2 else None
            right1 = node1.right if node1 else None
            right2 = node2.right if node2 else None
            
            root.left=fun(left1, left2)
            root.right=fun(right1, right2)
            return root
        return fun(root1,root2)
        