class MinHeap:
    def __init__(self,initial_data=None):
        self.data=[]

        if initial_data:
            self.data=list(initial_data)
            self.build_heap()

    def left_child(self,index):
        return 2*index+1

    def right_child(self,index):
        return index*2+2

    def parent(self,index):
        return (index-1)//2

    def build_heap(self):
        for i in range((len(self.data)-2)//2,-1,-1):
            self.heapify_down(i)


    def heapify_down(self,index):
        size=len(self.data)
        while True:
            right=self.right_child(index)
            left=self.left_child(index)

            small=index
            if left<size and self.data[small]>self.data[left]:
                small=left
            if right <size and self.data[small]> self.data[right]:
                small=right

            if index==small:
                break

            
            self.data[small],self.data[index]=self.data[index],self.data[small]
            index=small

    def heapify_up(self,index):
        while index>0:
            parent_index=self.parent(index)
            if self.data[index]<self.data[parent_index]:
                self.data[index],self.data[parent_index]=self.data[parent_index],self.data[index]
                index=parent_index
            else: 
                break


    def push(self,value):
        self.data.append(value)
        self.heapify_up(len(self.data)-1)


    def peek(self):
        if not self.data:
           raise IndexError("peek from empty heap")
        return self.data[0]    
    
    def pop(self):
        if not self.data:
           raise IndexError("pop from empty heap")
        self.data[-1],self.data[0]=self.data[0],self.data[-1]
        min_value=self.data.pop()
        if self.data:
           self.heapify_down(0)
        return min_value
    
    def len(self):
        return len(self.data)




def heapsort_inplace(arr):
    heap=MinHeap(arr)
    sorted_list=[]
    while heap.len()>0:
        sorted_list.append(heap.pop())


    return sorted_list    



arr=[4,9,3,8,7,5,6]
heap=MinHeap(arr)
for i in heap.data:
    print(i)

