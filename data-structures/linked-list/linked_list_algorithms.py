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

def nth_last_element(linked_list, n=1):
    head = linked_list.head
    if head.next_node == None:
        print("Only one node in the list")
        return head
    
    nth_node = head
    last_node = head
    node_distance = 0

    while last_node.next_node != None:
        last_node = last_node.next_node
        if node_distance >= n- 1:
            nth_node = nth_node.next_node
        node_distance += 1
    
    return nth_node.data

def middle_element(linked_list):
    head = linked_list.head
    if head.next_node == None:
        return head
    
    last_node = head
    middle_node = head

    while last_node.next_node != None:
        last_node = last_node.next_node
        if last_node.next_node != None:
            last_node = last_node.next_node
            middle_node = middle_node.next_node
    
    return middle_node.data
    


test_list = singly_linked_list(0)

for number in range(1,7):
    test_list.add_to_tail(Node(data=number))

print(test_list)

