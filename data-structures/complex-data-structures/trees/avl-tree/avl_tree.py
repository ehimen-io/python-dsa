from tree_node import Tree_Node

class AVL_Tree:
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
        self.update_balance_factors()
        self.root = self.rearrange_from(self.root)



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
        print(f"Starting from {current_node.data[1]}")
        while True:
            current_key = current_node.data[0]
            current_value = current_node.data[1]
            if current_key == target_key and current_value == value:
                return current_node.data
            elif target_key <= current_key and current_node.has_left_child():
                current_node = current_node.left_child
                print(f"{target_key} <= {current_key}. Go left")
            elif target_key > current_key and current_node.has_right_child():
                current_node = current_node.right_child
                print(f"{target_key} > {current_key}. Go right")
            else:
                print(f"No more child nodes found with value = {value}")
                return None
    
    def __str__(self) -> str:
        self.update_levels()
        return str(self.root)
    
    def left_rotate(self, target_node: Tree_Node):
        if not target_node.has_right_child():
            print(f"Cannot perform right rotation on Node {target_node.data}")
            return target_node
        
        new_root = target_node.right_child
        target_node.right_child = new_root.left_child
        new_root.left_child = target_node
        return new_root

    def right_rotate(self, target_node: Tree_Node):
        if not target_node.has_left_child():
            print(f"Cannot perform right rotation on Node {target_node.data}")
            return target_node
        
        new_root = target_node.left_child
        target_node.left_child = new_root.right_child
        new_root.right_child = target_node
        return new_root

    def left_right_rotate(self, target_node: Tree_Node):
        target_node.left_child = self.left_rotate(target_node.left_child)
        new_root = self.right_rotate(target_node)
        return new_root

    def right_left_rotate(self, target_node: Tree_Node):
        target_node.right_child = self.right_rotate(target_node.right_child)
        new_root = self.left_rotate(target_node)
        return new_root
    
    # For String representation
    def update_levels(self, iteration_num = 1):
        self.root.level = iteration_num - 1
        left_child = AVL_Tree()
        right_child = AVL_Tree()

        if self.root.has_left_child():    
            left_child.root = self.root.left_child
            left_child.update_levels(iteration_num=iteration_num + 1)
        
        if self.root.has_right_child():
            right_child.root = self.root.right_child
            right_child.update_levels(iteration_num=iteration_num + 1)
    
    def update_balance_factors(self):
        left_height = self.get_height(self.root.left_child)
        right_height = self.get_height(self.root.right_child)
        left_child = AVL_Tree()
        right_child = AVL_Tree()

        self.root.balance_factor = left_height - right_height

        if self.root.has_left_child():
            left_child.root = self.root.left_child
            left_child.update_balance_factors()
        
        if self.root.has_right_child():
            right_child.root = self.root.right_child
            right_child.update_balance_factors()

    def get_height(self, node: Tree_Node):
        if node == None:
            return -1
        elif not node.has_left_child() and not node.has_right_child():
            return 0
        else:
            left_child_height = self.get_height(node.left_child)
            right_child_height = self.get_height(node.right_child)
            return max([left_child_height, right_child_height]) + 1

    def rearrange_from(self, root: Tree_Node):
        new_root = root
        if root != None and root.has_children():
            root.left_child = self.rearrange_from(root.left_child)
            root.right_child = self.rearrange_from(root.right_child)
            if root.balance_factor > 1:
                if root.left_child.has_left_child():
                    new_root = self.right_rotate(target_node=root)
                else:
                    new_root = self.left_right_rotate(target_node=root)
            elif root.balance_factor < -1:
                if root.right_child.has_right_child():
                    new_root = self.left_rotate(target_node=root)
                else:
                    new_root = self.right_left_rotate(target_node=root)

        return new_root

        


test_tree = AVL_Tree()
test_tree.add_values(1,4,2,3,7,9,5)
print(test_tree)
test_tree.update_balance_factors()
print(f"Root Balance Factor: {test_tree.root.balance_factor}")


