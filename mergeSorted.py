from LinkedList import LinkedList

def merge_Sorted_Linked_List(list1: LinkedList,list2: LinkedList)->LinkedList:
     p1=list1.head
     p2=list2.head
     list3=LinkedList()
     while p1 and p2:
          if(p1.data<p2.data):
               list3.insert_at_last(p1.data)
               p1=p1.next


          else:
            list3.insert_at_last(p2.data)
            p2=p2.next
        
        
     if p1:
         list3.insert_at_last(p1.data)
     else:
         list3.insert_at_last(p2.data)


     return list3 
     


l1=LinkedList()
l1.insert_at_first(1)
l1.insert_at_last(3)
l1.insert_at_last(5)
l2=LinkedList()
l2.insert_at_first(2)
l2.insert_at_last(4)
l2.insert_at_last(6)
l3=merge_Sorted_Linked_List(l1,l2)
l3.display()

