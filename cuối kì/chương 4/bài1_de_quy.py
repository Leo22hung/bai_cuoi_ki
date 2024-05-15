class Node:
    def __init__(self, data):
        self.info = data
        self.next = None

class DanhSachLienKet:
    def __init__(self):
        self.head = None

    def Them(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def InNguoc_DeQui(self, node):
        if node is None:
            return
        self.InNguoc_DeQui(node.next)
        print(node.info, end=" ")

dslk = DanhSachLienKet()
dslk.Them(1)
dslk.Them(2)
dslk.Them(3)
dslk.Them(4)

print("In nguoc danh sach lien ket bang de qui:")
dslk.InNguoc_DeQui(dslk.head)

