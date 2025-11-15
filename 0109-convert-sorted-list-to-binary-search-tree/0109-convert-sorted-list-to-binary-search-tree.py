# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:

        cnt=0
        curr=head
        while curr:
            cnt+=1
            curr=curr.next
        
        self.curr=head
        def bt(n):
            if n<=0:
                return None
            
            left=bt(n//2)
            root=TreeNode(self.curr.val)
            self.curr=self.curr.next
            right=bt(n-n//2-1)
            root.left=left
            root.right=right
            return root
        
        return bt(cnt)
        