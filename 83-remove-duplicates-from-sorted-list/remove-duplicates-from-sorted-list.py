# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return None
        curr=fcurr=head
        while fcurr:
            if curr.val==fcurr.val:
                fcurr=fcurr.next
            else:
                curr.next=fcurr
                curr=fcurr
                fcurr=fcurr.next
        curr.next=fcurr
        return head
        
