class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

    def add_child_array(self, child_node_array):
        self.children = child_node_array

    def remove_child(self, child_node):
        self.children = [child for child in self.children if child != child_node]

    def get_children_array(self):
        return self.children
    
    def get_child(self, child_node):
        return self.children.get(child_node)

    def get_value(self):
        return self.value

    def traverse(self):
        print(self.value)
        for child in self.children:
            child.traverse()

print("Hello")