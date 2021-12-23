MAX_DEPTH = 4

class Node:
    def __init__(self, left=None, right=None, parent=None):
        self.left = left
        self.right = right
        self.parent = parent
    
    def __str__(self):
        return f"[{self.left}, {self.right}]"
    
    def get_left(self):
        return self.left
    
    def get_right(self):
        return self.right
    
    def get_parent(self):
        return self.parent
    
    def set_left(self, new_left):
        self.left = new_left
    
    def set_right(self, new_right):
        self.right = new_right
    
    def set_parent(self, new_parent):
        self.parent = new_parent

def create_tree_from_line(line):
    open_bracket_count = 0
    current_node = Node()
    previous_character = ""

    for character in line:
        if character == "[":
            open_bracket_count = open_bracket_count + 1
            if previous_character == ",":
                current_node.set_right(Node(parent=current_node))
                current_node = current_node.get_right()
            else:
                current_node.set_left(Node(parent=current_node))
                current_node = current_node.get_left()
        
        elif character == "]":
            open_bracket_count = open_bracket_count - 1
            current_node = current_node.get_parent()
        
        elif character == ",":
            pass

        elif previous_character == "[":  # Integer found
            current_node.set_left(int(character))

        else:  # Previous character was a comma
            current_node.set_right(int(character))
        
        previous_character = character

    current_node.get_left().set_parent(None)
    return current_node.get_left()  # TODO: Clean up so that this is not necessary

def explode_node(node):  # TODO: Integer not always imediate for opposite sides / not always [15,[0,13]], for example
    original_parent = node.get_parent()
    original_node = node
    print(node, original_parent.get_right())
    if node is original_parent.get_right():  # Input node is a right child
        parent = original_parent
        new_left = original_parent.get_left() + original_node.get_left()
        while parent is not None and parent.get_right() is node:
            node = parent
            parent = node.get_parent()
        if parent is not None:
            left = parent.get_right()
            if isinstance(left, int):
                parent.set_right(left + original_node.get_right())
            else:
                while isinstance(left, Node):
                    parent = left
                    left = parent.get_left()
                parent.set_left(left + original_node.get_right())
        
        original_parent.set_left(new_left)
        original_parent.set_right(0)
    
    else:  # Input node is a left child
        parent = original_parent
        new_right = original_parent.get_right() + original_node.get_right()
        while parent is not None and parent.get_left() is node:
            node = parent
            parent = node.get_parent()
        if parent is not None:
            right = parent.get_left()
            if isinstance(right, int):
                parent.set_left(right + original_node.get_left())
            else:
                while isinstance(right, Node):
                    parent = right
                    right = parent.get_right()
                parent.set_right(right + original_node.get_left())
        
        original_parent.set_left(0)
        original_parent.set_right(new_right)

def add_snailfish_numbers(tree1, tree2):
    new_tree = Node(tree1, tree2)
    tree1.set_parent(new_tree)
    tree2.set_parent(new_tree)
    return new_tree

def split_node(node, depth):
    if node.get_left() >= 10:
        original_value = node.get_left()
        divide_by_two_round_down = original_value // 2
        node.set_left(Node(divide_by_two_round_down, original_value-divide_by_two_round_down, node))
        new_node = node.get_left()
    else:  # Right is >= 10
        original_value = node.get_right()
        divide_by_two_round_down = original_value // 2
        node.set_right(Node(divide_by_two_round_down, original_value-divide_by_two_round_down, node))
        new_node = node.get_right()
    
    depth = depth + 1
    if depth >= MAX_DEPTH:  # New node must explode if it's depth exceeds the limit
        explode_node(new_node)

def depth_first_explode_search(tree, depth=0):
    left_not_searched = right_not_searched = True
    if isinstance(tree.get_left(), Node):
        depth_first_explode_search(tree.get_left(), depth+1)
        left_not_searched = False
    if isinstance(tree.get_right(), Node):
        depth_first_explode_search(tree.get_right(), depth+1)
        right_not_searched = False
    if left_not_searched and right_not_searched and depth >= MAX_DEPTH:
        print(tree)
        explode_node(tree)

def depth_first_split_search(tree, depth=0):
    left_not_searched = right_not_searched = True
    if isinstance(tree.get_left(), Node):
        depth_first_split_search(tree.get_left(), depth+1)
        left_not_searched = False
    if left_not_searched and tree.get_left() >= 10:
        split_node(tree, depth)
    
    if isinstance(tree.get_right(), Node):
        depth_first_split_search(tree.get_right(), depth+1)
        right_not_searched = False
    if right_not_searched and tree.get_right() >= 10:
        split_node(tree, depth)


with open("day18.txt", "r") as file:
    line = file.readline().strip()
    tree = create_tree_from_line(line)
    for line in file:
        tree_to_add = create_tree_from_line(line.strip())
        tree = add_snailfish_numbers(tree, tree_to_add)
        print(tree)
        depth_first_explode_search(tree)
        depth_first_split_search(tree)
        print(tree)
    # test_node = tree.get_left().get_right().get_right().get_right()
    # print(test_node)
    # explode_node(test_node)
    # print(tree)
