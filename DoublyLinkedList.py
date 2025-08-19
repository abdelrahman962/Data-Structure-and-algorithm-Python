class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev=None





class Doubly:
    def __init__(self):
        self.head=None

    def insert_at_first(self,data):
        newNode=Node(data)
        if self.head==None:
            self.head=newNode
            return
        newNode.next=self.head
        self.head.prev=newNode
        self.head=newNode
        

    def insert_at_end(self,data):
        newNode=Node(data)
        if self.head==None:
            self.head=newNode
            return
        current=self.head
        while current.next:
           
            current=current.next

        current.next=newNode
        newNode.prev=current

    def traverse(self):
        current=self.head
        while current:
            print(current.data,"-->")
            current=current.next

    def traverse1(self):
        current=self.head
        while current.next:
           
            current=current.next


        while current:
            print(current.data,"-->")
            current=current.prev



d=Doubly()
d.insert_at_first(9)
d.insert_at_first(8)
d.insert_at_first(7)
d.traverse()

print("____________")
d.traverse1()

d.insert_at_end(10)
d.traverse()