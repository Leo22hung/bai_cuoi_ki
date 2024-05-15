class Node:
    def __init__(self, data):
        self.info = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def copyHelper(self, node):
        if node is None:
            return None
        new_node = Node(node.info)
        new_node.left = self.copyHelper(node.left)
        new_node.right = self.copyHelper(node.right)
        return new_node

    def Chep(self):
        new_tree = BinaryTree()
        new_tree.root = self.copyHelper(self.root)
        return new_tree

tree = BinaryTree()
tree.root = Node(1)
tree.root.left = Node(2)
tree.root.right = Node(3)

copied_tree = tree.Chep()

def printTree(node):
    if node is not None:
        print(node.info, end=" ")
        printTree(node.left)
        printTree(node.right)

print("Cây gốc:")
printTree(tree.root)
print("\nCây được sao chép:")
printTree(copied_tree.root)
