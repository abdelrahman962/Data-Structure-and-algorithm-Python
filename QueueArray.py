class QueueArray:
    def __init__(self, capacity):
        self.queue = [None] * capacity
        self.capacity = capacity
        self.front = 0
        self.rear = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    def enqueue(self, data):
        if self.is_full():
            print("Error: Queue is full")
            return
        self.queue[self.rear] = data
        self.rear = (self.rear + 1) % self.capacity
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            print("Error: Queue is empty")
            return
        removed = self.queue[self.front]
        self.queue[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return removed    
    
    def peek(self):
         if self.is_empty():
            print("Error: Queue is empty")
            return
         return self.queue[self.front]
    

    # def dequeue(self):
    #     if self.is_empty():
    #         print("Error: Queue is empty")
    #         return

    #     removed = self.queue[self.front]

    #     for i in range(1, self.size):
    #         self.queue[i - 1] = self.queue[i]

    #     self.queue[self.size - 1] = None
    #     self.size -= 1
    #     self.rear -= 1

    #     return removed
