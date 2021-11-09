from node import Node

class singly_linked_list:
    def __init__(self, head_data):
        self.head = Node(head_data)
    
    def add_to_tail(self, new_node):
        if type(new_node) != Node:
            raise TypeError("New Node is not valid")
        else:
            current_tail = self.head
            while current_tail.next_node != None:
                current_tail = current_tail.next_node
            current_tail.next_node = new_node
    
    
    def add_to_head(self, new_head):
        if type(new_head) != Node:
            raise TypeError("New Node is not valid")
        else:
            current_head = self.head
            new_head.next_node = current_head
            self.head = new_head
    
    def remove_head(self):
        previous_head = self.head
        next_head = previous_head.next_node
        self.head = next_head
        return previous_head

    def __str__(self):
        return str(self.head)
    
        

list = singly_linked_list("I am the head node")
list.add_to_tail(Node(data="I am the second node"))
list.add_to_tail(Node(data="I am the final"))
list.add_to_head(Node(data="I am now the new head"))

print(list)

removed_head = list.remove_head()

print(list)