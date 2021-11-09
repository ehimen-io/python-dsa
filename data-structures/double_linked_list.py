class Node:
    def __init__(self, data, next_node = None, previous_node = None):
        self.data = data
        self.next = next_node
        self.prev = previous_node
    
    def __str__(self):
        return f"({self.data}) <-> {self.next}"

class doubly_linked_list:
    def __init__(self, head_data):
        self.head = Node(head_data)
        self.tail = self.head
    
    def add_to_tail(self, new_tail):
        if type(new_tail) != Node:
            print("New tail is not a node")
            return
        
        current_tail = self.tail
        new_tail.prev = current_tail
        current_tail.next = new_tail
        self.tail = new_tail
    
    def add_to_head(self, new_head):
        if type(new_head) != Node:
            print("New head is not a node")
            return
        
        current_head = self.head
        new_head.next = current_head
        current_head.prev = new_head
        self.head = new_head
    
    def add_to_position(self, new_node, position = -1):
        if position == -1 or self.head.next == None:
            self.add_to_tail(new_node)
            return

        if position == 0:
            self.add_to_head(new_node)
            return

        current = self.head
        prev = None
        current_position = 0

        while current_position < position:
            prev = current
            current = current.next
            if current == None:
                print(f"Position {position} is out of bounds")
                return
            current_position += 1
        
        new_node.next = current
        new_node.prev = prev
        current.prev = new_node
        prev.next = new_node

    def get_node_at(self, position=0):
        if position == -1 or self.head.next == None:
            return self.tail.data
        
        if position == 0:
            return self.head.data
        
        current = self.head
        current_position = 0

        while current_position < position:
            current = current.next
            if current == None:
                print(f"Position {position} is out of bounds")
                return
            current_position += 1
        
        return current.data
    
    def __str__(self):
        return f"None <-> {str(self.head)}"
