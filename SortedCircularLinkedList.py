from Node import Node


class SortedCircularLinkedList:
    def __init__(self):
        self.head=None

    def insert_sorted(self,data):
        new_node=Node(data)
        if self.head==None:
            self.head=new_node
            self.head.next=self.head
            return

        current=self.head
        if new_node.data <=current.data:
           while current.next!=self.head:
               current=current.next
           new_node.next=current.next
           current.next=new_node
           self.head=new_node   
           return
        while current.next!=self.head and current.next.data<new_node.data:
            current=current.next

        if current.next==self.head:
             new_node.next=current.next
             current.next=new_node
             return
        
        new_node.next=current.next
        current.next=new_node

    def printList(self):

        current=self.head
        while True:
            print(current.data,"->")
            current=current.next
            if current.next==self.head:
                print(current.data)
                return


            

        

s=SortedCircularLinkedList()
s.insert_sorted(7)
s.insert_sorted(3)
s.insert_sorted(9)
s.insert_sorted(1)
s.insert_sorted(4)
s.printList()