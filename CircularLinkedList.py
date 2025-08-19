from Node import Node


class CircularLinkedList:
    def __init__(self):
        self.head=None






    def insert(self,data):
        newNode=Node(data)
        if self.head==None:
            self.head=newNode
            self.head.next=self.head
            return
        newNode.next=self.head
        current=self.head
        while True:
            if current.next==self.head:
                break
            current=current.next

        current.next=newNode   


    def printList(self):

        current=self.head
        while True:
            print(current.data,"->")
            current=current.next
            if current==self.head:
                return
            
    def length(self):
        count=0
        current=self.head
        if self.head==None:
            return 0
        while True:
            count+=1
            current=current.next
            if current==self.head:
                return count
        
    def elimination(self,k):
        current=self.head     
        while current.next!=current: 
            for i in range(0,k-2):
                current=current.next
            current.next=current.next.next
            current=current.next
        self.head=current    





c=CircularLinkedList()



for i in range(1,6):
    c.insert(i)



c.printList()

c.elimination(3)

print("_________________________________")
c.printList()
