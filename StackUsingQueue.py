

from QueueList import QueueList

class StackUsingQueue:
    def __init__(self):
        self.q1=QueueList()
        self.q2=QueueList()

    def push(self,data):
        self.q1.enqueue(data)
        while not self.q2.is_empty():
                self.q1.enqueue(self.q2.dequeue())
                    
        self.q2,self.q1=self.q1,self.q2


    def pop(self):
        if self.q2.is_empty():
            print("Stack is empty")
            return None
        return self.q2.dequeue()

    def is_empty(self):
        return  self.q2.is_empty()
    
    def peek(self):
         return self.q2.peek()



from collections import deque

class Stack_queue:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, data):
        # أضف العنصر الجديد إلى q1
        self.q1.append(data)

        # انقل كل عناصر q2 إلى q1
        while self.q2:
            self.q1.append(self.q2.popleft())

        # بدّل q1 و q2
        self.q1, self.q2 = self.q2, self.q1

    def pop(self):
        if not self.q2:
            print("Stack is empty")
            return None
        return self.q2.popleft()

    def is_empty(self):
        return not self.q2

    def peek(self):
        if not self.q2:
            print("Stack is empty")
            return None
        return self.q2[0]





s=StackUsingQueue()
s.push(1)
s.push(2)
s.push(3)



print(s.pop())
print(s.peek())
