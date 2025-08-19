class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def middleNode(self, head):
        slow = head
        fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        return slow

        

 
l1=ListNode(1)
l2=ListNode(2)
l3=ListNode(3)
l4=ListNode(4)
l5=ListNode(5)
l1.next=l2
l2.next=l3
l3.next=l4
l4.next=l5
s=Solution()
print(s.middleNode(l1))

