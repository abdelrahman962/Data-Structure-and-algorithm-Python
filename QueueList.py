from Node import Node
class QueueList:
    def __init__(self):
        self.head=None
        self.rear=None

    def is_empty(self):
        return self.head==None

    def enqueue(self,data):
        new_node=Node(data)
        if self.is_empty():
            self.head=self.rear=new_node
            return
        self.rear.next=new_node
        self.rear=self.rear.next

    def dequeue(self):
        if self.is_empty():
            print("Error: Queue is empty")
            return
        removed=self.head.data
        self.head=self.head.next
        if self.head==None:
            self.rear=None
        
        return removed
    

    def peek(self):
        if self.is_empty():
            print("Error: Queue is empty")
            return
        return self.head.data



print_queue = QueueList()

def add_print_job(job):
    print_queue.enqueue(job)
    print(f"Added print job: {job}")

def print_job():
    job = print_queue.dequeue()
    if job:
        print(f"Printing job: {job}")



def main():
    add_print_job("Document1.pdf")
    add_print_job("Photo.png")
    add_print_job("Invoice.docx")

    print_job()  # Should print "Document1.pdf"
    print_job()  # Should print "Photo.png"

    add_print_job("Presentation.pptx")

    print_job()  # Should print "Invoice.docx"
    print_job()  # Should print "Presentation.pptx"

    print_job()  # Queue is empty, should print error

if __name__ == "__main__":
    main()
