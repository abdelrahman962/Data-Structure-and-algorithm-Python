
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        result=ListNode(0)
        current=result
        carry=0
        x=0
        y=0
        while l1!=None  or l2!=None or carry!=0:
            if  l1:
                x=l1.val
            else:
                x=0

            if  l2:
                y=l2.val
            else:
                y=0
            sum=x+y+carry
            carry=sum//10    
            current.next=ListNode(sum%10)
            current=current.next
            if l1:
                l1=l1.next
          

            if l2:
                l2=l2.next
         
            
        return result.next  
 


 

 # Helper function to create linked list from list
def create_list(nums):
    dummy = ListNode(0)
    curr = dummy
    for num in nums:
        curr.next = ListNode(num)
        curr = curr.next
    return dummy.next

# Helper function to print linked list
def print_list(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")

# Example
l1 = create_list([2,4,3])  # 342
l2 = create_list([5,6,4])  # 465

sol = Solution()
res = sol.addTwoNumbers(l1, l2)  # Expected: 7 -> 0 -> 8
print_list(res)
