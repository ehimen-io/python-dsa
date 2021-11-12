class Tree_Node:
    def __init__(self, data, level = 0):
        self.data = data
        self.level = level
        self.balance_factor = 0
        self.left_child = None
        self.right_child = None

    def set_left_child(self, data):
        self.left_child = Tree_Node(data, level= self.level + 1)
        return self.left_child
    
    def set_right_child(self, data):
        self.right_child = Tree_Node(data, level= self.level + 1)
        return self.right_child
    
    def has_left_child(self):
        return self.left_child != None
    
    def has_right_child(self):
        return self.right_child != None

    def has_children(self):
        return self.has_left_child() or self.has_right_child()

    def __str__(self):
        level_string = ''.join(["--" for num in range(self.level + 1)])
        left_child = self.left_child if self.has_left_child() else "()"
        right_child = self.right_child if self.has_right_child() else "()"

        if type(self.data) == tuple:
            return f"{self.data[1]}\n{level_string}{left_child}\n{level_string}{right_child}"

        return f"{self.data}\n{level_string}{left_child}\n{level_string}{right_child}"

