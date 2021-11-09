from node import Node
from linked_list import singly_linked_list

def swap_nodes(linked_list, first_node, second_node):
    node_1 = linked_list.head
    node_2 = linked_list.head
    prev_node_1 = None
    prev_node_2 = None
    next_node_1 = linked_list.head.next_node
    next_node_2 = linked_list.head.next_node

    if linked_list.head.next_node == None:
        return linked_list
    
    if first_node == second_node:
        print("Nodes are the same")
        return linked_list

    while node_1.data != first_node or node_2.data != second_node:
        if node_1.data != first_node:
            prev_node_1 = node_1
            node_1 = node_1.next_node
            next_node_1 = node_1.next_node
        
        if node_2.data != second_node:
            prev_node_2 = node_2
            node_2 = node_2.next_node
            next_node_2 = node_2.next_node
        
        if node_1.next_node == None or node_2.next_node == None:
            break
    
    if node_1.data != first_node or node_2.data != second_node:
        print("Node pair not found")
        return linked_list
    
    node_1.next_node = next_node_2
    node_2.next_node = next_node_1

    if prev_node_1 != None:
        prev_node_1.next_node = node_2
    else:
        linked_list.head = node_2

    if prev_node_2 != None:
        prev_node_2.next_node = node_1
    else:
        linked_list.head = node_1
    
    return linked_list





test_list = singly_linked_list(-1)

for number in range(7):
    test_list.add_to_tail(Node(data=number))

print(test_list)

swapped_list = swap_nodes(test_list, first_node=-1, second_node=4)
print(swapped_list)

