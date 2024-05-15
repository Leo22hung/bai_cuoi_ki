class Node:
    def __init__(self, data):
        self.info = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def ChieuCao(self, node):
        if node is None:
            return 0
        else:
            return max(self.ChieuCao(node.left), self.ChieuCao(node.right)) + 1

    def height(self):
        return self.ChieuCao(self.root)

tree = BinaryTree()
tree.root = Node(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

print("Chiều cao của cây:", tree.height())
