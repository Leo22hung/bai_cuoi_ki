class Node:
    def __init__(self, data):
        self.info = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def isBSTUtil(self, node, min_val, max_val):
        if node is None:
            return True

        if node.info < min_val or node.info > max_val:
            return False

        return (self.isBSTUtil(node.left, min_val, node.info - 1) and
                self.isBSTUtil(node.right, node.info + 1, max_val))

    def KiemTraBST(self):
        return self.isBSTUtil(self.root, float("-inf"), float("inf"))

tree = BinaryTree()
tree.root = Node(4)
tree.root.left = Node(2)
tree.root.right = Node(5)
tree.root.left.left = Node(1)
tree.root.left.right = Node(3)

if tree.KiemTraBST():
    print("Cây là một cây BST")
else:
    print("Cây không phải là một cây BST")
