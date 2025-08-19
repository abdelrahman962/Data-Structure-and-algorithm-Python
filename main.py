from LinkedList import LinkedList
from Node import Node
# def merge_Sorted_Linked_List(list1,list2):
#      p1=list1.head
#      p2=list2.head
#      list3=LinkedList()
#      while p1 and p2:
#           if(p1.data<p2.data):
#                list3.insert_at_last(p1.data)
#                p1=p1.next


#           else:
#             list3.insert_at_last(p2.data)
#             p2=p2.next
        
        
#      if p1:
#          list3.insert_at_last(p1.data)
#      else:
#          list3.insert_at_last(p2.data)


#      return list3 
     


def check(l1):
    slow=l1.head
    fast=l1.head
    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next
        if slow==fast:
            return True

    return False

def check2(l1):
    current=l1.head.next
    while current!=l1.head and current!=None:
        current=current.next

    return current!=None









l1=LinkedList()
l1.insert_at_last(5)
l1.insert_at_last(2)
l1.insert_at_last(3)
l1.insert_at_last(1)

l1.display()
print("min sum : ",l1.reduce_to_non_decreasing())

l1.display()