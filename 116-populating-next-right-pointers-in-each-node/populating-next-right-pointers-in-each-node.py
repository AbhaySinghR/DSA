"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':

        curr=root
        while curr:
            dummy=Node(0)
            itr=dummy
            while curr:
                if curr.left:
                    itr.next=curr.left
                    itr=curr.left
                if curr.right:
                    itr.next=curr.right
                    itr=curr.right
                curr=curr.next
            curr=dummy.next
        
        return root


        