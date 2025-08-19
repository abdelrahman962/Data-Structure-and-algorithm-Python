
from Node import Node
class QueueCustomers:
    def __init__(self):
        self.head=None
        self.rear=None

    def enqueue(self,name):     
         new_node=Node(name)

         if self.head==None:
             self.head=self.rear=new_node
             return


         self.rear.next=new_node
         
         self.rear=self.rear.next


    def dequeue(self):
        if self.is_empty():
         
            return
        removed=self.head.data
        self.head=self.head.next
        return removed

    def is_empty(self):
        return self.head==None
    

def customerSimulation(nameList):
        q=QueueCustomers()
        for name in nameList:
           q.enqueue(name)
           print("Arriving: "+name)
           
                    
        while not q.is_empty():

           n= q.dequeue()
           print("Serving: "+n)



        print("All customers served.")    





nameList=["Alice", "Bob", "Carol"]         
customerSimulation(nameList)

