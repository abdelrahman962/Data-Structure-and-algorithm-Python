class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev=None





class CircularLinkedList:
    def __init__(self):
        self.head=None



    def insert_at_first(self,data):
        newNode=Node(data)
        if self.head==None:
            self.head=newNode
            self.head.next=self.head
            return
        newNode.next=self.head
        newNode.prev=self.head.prev
        self.head.prev=newNode
        newNode.prev.next=newNode

        self.head=newNode
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
            print("next: ",current.data,"->")

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
        


c=CircularLinkedList()
n1=Node(9)
n2=Node(1)
n3=Node(5)
n1.next=n2
n2.next=n3
n3.next=n1
c.head=n1





c.printList()

