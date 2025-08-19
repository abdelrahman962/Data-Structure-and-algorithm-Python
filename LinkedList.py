from Node import Node
class LinkedList:
    def __init__(self):
        self.head = None


    def insert_at_first(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
             

    def insert_at_last(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head = new_node
            return self.head
        last_node = self.head
        if last_node is not None:
            while last_node.next:
                last_node = last_node.next
            last_node.next=new_node
       
    def insert_between(self,index,data):
        new_node=Node(data)
        if index == 0:
            self.insert_at_first(data)
            return
        count=0
        current=self.head
        while current is not None and count < index-1:
            current = current.next
            count += 1
        if current is None:
            print("Index out of bounds")
            return      
        new_node.next = current.next
        current.next = new_node

     
    def display(self):
        print(self.__str__())    

    def __str__(self):
        res=""
        temp=self.head
        while temp:
            res += str(temp.data) + "  "
            temp = temp.next
        return res 
    def delete_at_first(self):
        if self.head is None:
            return
        self.head=self.head.next
    def delete_at_last(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
            return
        second_last = self.head
        while second_last.next.next:
            second_last = second_last.next
        second_last.next = None
       
    def length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count
    def find_middle1(self):
        current=self.head
        count=self.length()//2
        for i in range(0,count):
            current=current.next

        return current.data    


    def find_middle2(self):
        p1=self.head
        p2=p1.next
        while p2:
            p1=p1.next
            p2=p2.next.next
        return p1.data    

           
    def merge_Sorted_Linked_List(self,list1,list2):
       p1=list1.head
       p2=list2.head
       list3=LinkedList()
       while p1 and p2:
          if(p1.data<p2.data):
               list3.insert_at_last(p1.data)
               p1=p1.next


          else:
            list3.insert_at_last(p2.data)
            p2=p2.next
        
        
          if p1:
            list3.insert_at_last(p1.data)
          else:
            list3.insert_at_last(p2.data)


          return list3 
     
    def remove_duplicates(self):
        p1=self.head
        p2=self.head.next
        while p2:
            if p1.data==p2.data:
                p1.next=p2.next
                p2=p2.next
            else:
               p1=p1.next
               p2=p2.next

    def reversed_Linked_List(self):
        prev=None 
        current=self.head
        after=current 
        while current!= None:
            after=current.next
            current.next=prev
            prev=current
            current=after
        self.head=prev
            




    def merge_Sorted_Linked_List(self,list2):
      p1=self.head
      p2=list2.head
      list3=LinkedList()
      while p1 and p2:
          if(p1.data<p2.data):
               list3.insert_at_last(p1.data)
               p1=p1.next


          else:
            list3.insert_at_last(p2.data)
            p2=p2.next
        
        
      if p1:
         list3.insert_at_last(p1.data)
      else:
         list3.insert_at_last(p2.data)

      self.head=list3.head


    def is_non_decreasing(self):
        current=self.head
        while current and current.next:
            if current.data<current.next.data:
                return False
            current=current.next
        return True


    def find_min_sum_pair(self):
        p1=self.head
 
        min=float('inf')
        min_prev=None
        prev=None
        while p1 and p1.next:
            sum=p1.data+p1.next.data
            if sum<min:
                sum=min
                min_prev=prev
            prev=p1
            p1=p1.next

        return min_prev         


    def insertion_sort(self):
        sortedList=None
        temp=self.head

        while temp:
            next_node=temp.next
            if sortedList is None or temp.data>=next_node.data:
                sortedList=temp
                

    def is_non_decreasing(self):
        current=self.head
        while current and current.next:
            if current.data>current.next.data:
                return False
            current=current.next
        return True

    def reduce_to_non_decreasing(self):
        operations=0
        while not self.is_non_decreasing():
            self.min_summation()
            operations+=1
        return operations    





    def min_summation(self):

        first=None
        second=None
        
        current=self.head
        min_sum= float('inf')
    
        while current and current.next :
            sum=current.data+current.next.data
            if sum<=min_sum:
                min_sum=sum
                first=current
                second=current.next
            current=current.next    

        new_node=Node(min_sum)
        current=self.head
        while current.next!=first:
            current=current.next
        new_node.next=second.next    
        current.next=new_node