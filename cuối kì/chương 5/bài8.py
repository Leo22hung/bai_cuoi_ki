class Node:
    def __init__(self, data):
        self.info = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def isIdentical(self, root1, root2):
        if root1 is None and root2 is None:
            return True
        if root1 is not None and root2 is not None:
            return (root1.info == root2.info and
                    self.isIdentical(root1.left, root2.left) and
                    self.isIdentical(root1.right, root2.right))
        return False

    def SoSanh(self, tree2):
        return self.isIdentical(self.root, tree2.root)

tree1 = BinaryTree()
tree1.root = Node(1)
tree1.root.left = Node(2)
tree1.root.right = Node(3)

tree2 = BinaryTree()
tree2.root = Node(1)
tree2.root.left = Node(2)
tree2.root.right = Node(3)

if tree1.SoSanh(tree2):
    print("Cây 1 và cây 2 giống nhau.")
else:
    print("Cây 1 và cây 2 không giống nhau.")
