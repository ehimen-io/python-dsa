class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

    def __str__(self):
        return f"({self.data}) -> {self.next}"

class queue:
    def __init__(self, max_length = None):
        self.max_length = max_length
        self.head = None
        self.tail = self.head
        self.size = 0
    
    def enqueue(self, *args):
        for data in args:
            if self.size == 0:
                self.head = Node(data)
                self.tail = self.head
                self.size += 1
            elif not self.isFull():
                new_tail = Node(data)
                current_tail = self.tail
                current_tail.next = new_tail
                self.tail = new_tail
                self.size += 1
            else:
                print(f"Cannot add Node({data}), queue is full.")
                break
            

    def dequeue(self):
        head = self.head
        if not self.isEmpty():
            self.head = head.next
        else:
            print("Queue is empty")
        
        return head

    def peek(self):
        return self.head.data

    def isFull(self):
        if self.max_length != None:
            return self.size >= self.max_length
        else:
            return False
    
    def isEmpty(self):
        return self.size == 0
    
    def __str__(self):
        return str(self.head)
