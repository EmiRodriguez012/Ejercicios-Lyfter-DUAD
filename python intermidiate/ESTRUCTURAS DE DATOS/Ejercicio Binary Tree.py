class Node:
    data: str

    def __init__(self, data, right=None, left=None):
        self.data = data
        self.right = right
        self.left = left

class BinaryTree: 

    root: Node

    def __init__(self, root):
        self.root= root

    def insert_node(self, new_node):
        current_node = self.root 

        while True:
            if new_node.data < current_node.data:
                if current_node.left is not None:
                    current_node = current_node.left
                else:
                    current_node.left = new_node
                    break

            else:
                if current_node.right is not None:
                    current_node = current_node.right
                else:
                    current_node.right = new_node
                    break

    def print_structure(self, node):
        if node is not None:
            self.print_structure(node.left)
            print(node.data)
            self.print_structure(node.right)
                



node_1 = Node("Soy el primer Nodo")
node_2 = Node("Soy el segundo Nodo")
node_3 = Node("Soy el tercer Nodo")
node_4 = Node("Soy el cuarto Nodo")
node_5 = Node("Soy el quinto Nodo")
node_6 = Node("Soy el sexto Nodo")

tree = BinaryTree (node_1)

tree.insert_node(node_2)

tree.print_structure(tree.root)

tree.insert_node(node_3)

tree.insert_node(node_4)

tree.insert_node(node_5)

tree.insert_node(node_6)



tree.print_structure(tree.root)

            
            




