class Node:
    def __init__(self, data):
        self.info = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def BSTTuanTu(self, node):
        if node is None:
            return True
        if node.left is not None and node.right is not None:
            return False
        return self.BSTTuanTu(node.left) and self.BSTTuanTu(node.right)

tree = BinaryTree()
tree.root = Node(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

if tree.BSTTuanTu(tree.root):
    print("Cây là cây BST tuần tự.")
else:
    print("Cây không là cây BST tuần tự.")
