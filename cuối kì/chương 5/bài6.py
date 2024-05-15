class Node:
    def __init__(self, data):
        self.info = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def height(self, node):
        if node is None:
            return 0
        return max(self.height(node.left), self.height(node.right)) + 1

    def isBalanced(self, node):
        if node is None:
            return True

        left_height = self.height(node.left)
        right_height = self.height(node.right)

        if abs(left_height - right_height) <= 1 and self.isBalanced(node.left) and self.isBalanced(node.right):
            return True

        return False

    def KiemTraAVL(self):
        return self.isBalanced(self.root)

tree = BinaryTree()
tree.root = Node(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.left.left = Node(5)

if tree.KiemTraAVL():
    print("Cây là một cây AVL")
else:
    print("Cây không phải là một cây AVL")
