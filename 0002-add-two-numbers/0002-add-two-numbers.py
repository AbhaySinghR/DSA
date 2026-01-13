# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        c1=l1
        c2=l2
        carry=0
        head3 = None
        c3= None

        while c1 and c2:
            s= c1.val + c2.val + carry
            if s >= 10:
                b = s % 10
                carry =1 
            else:
                b= s
                carry = 0
            
            if head3 is None:
                head3 = ListNode(b)
                c3 = head3
            
            else:
                temp = ListNode(b)
                c3.next = temp
                c3 = temp
            c1=c1.next
            c2=c2.next
        
        while c1:
            s = c1.val + carry
            if s >=10:
                b= s%10
                carry=1
            else:
                b = s
                carry=0
            
            temp=ListNode(b)
            c3.next=temp
            c3=temp
            c1=c1.next
        
        while c2:
            s = c2.val + carry
            if s >= 10:
                b= s%10
                carry=1
            else:
                b = s
                carry=0
            
            temp=ListNode(b)
            c3.next=temp
            c3=temp
            c2=c2.next
        
        if carry==1:
            temp=ListNode(1)
            c3.next=temp
            c3=temp
            c3.next=None
        else:
            c3.next=None
        
        return head3


        