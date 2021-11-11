from random import randint

class Tree_Node:
    def __init__(self, data, height = 0):
        self.data = data
        self.height = height
        self.left_child = None
        self.right_child = None

    def set_left_child(self, data):
        self.left_child = Tree_Node(data, height= self.height + 1)
        return self.left_child
    
    def set_right_child(self, data):
        self.right_child = Tree_Node(data, height= self.height + 1)
        return self.right_child
    
    def has_left_child(self):
        return self.left_child != None
    
    def has_right_child(self):
        return self.right_child != None
    
    def has_parent(self):
        return self.height != 0

    def __str__(self):
        height_string = ''.join(["--" for num in range(self.height + 1)])
        left_child = self.left_child if self.has_left_child() else "()"
        right_child = self.right_child if self.has_right_child() else "()"

        if type(self.data) == tuple:
            return f"{self.data[1]}\n{height_string}{left_child}\n{height_string}{right_child}"

        return f"{self.data}\n{height_string}{left_child}\n{height_string}{right_child}"

class Binary_Seach_Tree:
    def __init__(self):
        self.root = None
    
    def add(self, value):
        key = self.hash(value)
        if self.root == None:
            self.root = Tree_Node((key, value))
        else:
            current_node = self.root
            found = False
            while not found:
                current_key = current_node.data[0]
                if key > current_key:
                    if current_node.has_right_child():
                        current_node = current_node.right_child
                    else:
                        current_node.set_right_child((key, value))
                        found = True
                else:
                    if current_node.has_left_child():
                        current_node = current_node.left_child
                    else:
                        current_node.set_left_child((key, value))
                        found = True

    def add_values(self, *args):
        for value in args:
            self.add(value)

    def hash(self, value):
        hash_code = 0
        if type(value) == str:
            for character in value:
                hash_code += ord(character)
        else:
            hash_code = value
        return hash_code

    def search_for(self, value):
        current_node = self.root
        target_key = self.hash(value)
        #print(f"Starting from {current_node.data[1]}")
        while True:
            current_key = current_node.data[0]
            current_value = current_node.data[1]
            if current_key == target_key and current_value == value:
                return current_node.data
            elif target_key <= current_key and current_node.has_left_child():
                current_node = current_node.left_child
                #print(f"{target_key} <= {current_key}. Go left")
            elif target_key > current_key and current_node.has_right_child():
                current_node = current_node.right_child
                #print(f"{target_key} > {current_key}. Go right")
            else:
                #print(f"No more child nodes found with value = {value}")
                return None
    def __str__(self) -> str:
        return str(self.root)

