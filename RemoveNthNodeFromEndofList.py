

class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        current=head
        size=0
        while current!=None:
            size+=1
            current=current.next
        if size == n:
           return head.next
        index=size-n

        current=head
        for i in range(0,index-1):
            current=current.next

        current.next=current.next.next    

        return head
    
