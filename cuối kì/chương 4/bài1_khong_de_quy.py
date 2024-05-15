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

    def InNguoc_KhongDeQui(self):
        if self.head is None:
            return
        
        stack = []
        current = self.head
        while current:
            stack.append(current.info)
            current = current.next
        
        while stack:
            print(stack.pop(), end=" ")

dslk = DanhSachLienKet()
dslk.Them(1)
dslk.Them(2)
dslk.Them(3)
dslk.Them(4)

print("In nguoc danh sach lien ket khong de qui:")
dslk.InNguoc_KhongDeQui()
