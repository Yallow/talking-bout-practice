class SinglyLinkedList:
    #constructor
    def __init__(self):
        self.head = None
        
    #method for setting the head of the Linked List
    def setHead(self,head):
        self.head = head
    
    def find_middle_node(self):
        counter = 0
        root = self.head
        while self.head.next:
            self.head = self.head.getNext()
            counter += 1
        self.head = root
        counter = int(counter/2)
        for _ in range(counter):
            self.head = self.head.getNext()
        return self.head
            