

class FifoStack:
    def __init__(self):
        self.stack_in=[]
        self.stack_out=[]

    def enqueue(self,data):
        self.stack_in.append(data)

    def dequeue(self):
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        if self.stack_out:
            return self.stack_out.pop()
        return None             
    

    def is_empty(self):
        return not self.stack_in and self.stack_out
    
    def peek(self):
        if not self.stack_out:
            return
        
        return self.stack_out.pop()


