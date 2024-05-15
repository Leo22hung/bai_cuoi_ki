class Node:
    def __init__(self, data):
        self.info = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def chieucao(self, node):
        if node is None:
            return 0
        return 1 + max(self.chieucao(node.left), self.chieucao(node.right))

    def CanBangHoanToan(self, node):
        if node is None:
            return True
        left_height = self.chieucao(node.left)
        right_height = self.chieucao(node.right)
        if abs(left_height - right_height) <= 1 and self.CanBangHoanToan(node.left) and self.CanBangHoanToan(node.right):
            return True
        return False

tree = BinaryTree()
tree.root = Node(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.right = Node(6)

if tree.CanBangHoanToan(tree.root):
    print("Cây là cây cân bằng hoàn toàn.")
else:
    print("Cây không là cây cân bằng hoàn toàn.")
