from Node import Node

class StackList:
    def __init__(self):
        self.top=None


    def push(self,data):
        new_node=Node(data)
        new_node.next=self.top
        self.top=new_node


    def pop(self):
        if self.top is None:
            print("stack is empty")
            return
        temp=self.top
        self.top=self.top.next
        return temp.data

    def peek(self):
        if self.top:
           return self.top.data
        return None  

    def is_empty(self):
        return self.top is None

    def clear(self):
        if self.top:
           self.top=None         

           