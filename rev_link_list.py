class SinglyLinkedList:
    #constructor
    def __init__(self):
        self.head = None
        
    #method for setting the head of the Linked List
    def setHead(self,head):
        self.head = head
                      
    def reverse(self):
        last = None
        current = self.head

        while(current is not None):
            next = current.getNext()
            current.setNext(last)
            last = current
            current = next
        self.head = last
