class Node:
    def __init__(self, data, next_node = None):
        self.data = data
        self.next_node = next_node

    def __str__(self):
        return f"({self.data}) -> {self.next_node}"