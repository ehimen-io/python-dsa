class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

    def __str__(self):
        return f"({self.data}) -> {self.next}"

class Stack:
    def __init__(self, max_size = None):
        self.max_size = max_size
        self.head = None
        self.size = 0
    
    def push(self, *args):
        for data in args:
            if self.size == 0:
                self.head = Node(data)
                self.size += 1
            elif not self.isFull():
                current_head = self.head
                new_head = Node(data, next=current_head)
                self.head = new_head
                self.size += 1
            else:
                print(f"Cannot push any more data, stack is full")
                break
    
    def pop(self):
        head = self.head
        if not self.isEmpty():
            new_head = head.next
            self.head = new_head
        else:
            print("Stack is Empty")
        
        return head.data

    def peek(self):
        return self.head.data

    def isFull(self):
        if self.max_size != None:
            return self.size >= self.max_size
        else:
            return False
    
    def isEmpty(self):
        return self.size == 0
    
    def __str__(self):
        return str(self.head)

test_stack = Stack()