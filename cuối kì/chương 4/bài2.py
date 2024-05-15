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

    def DaoNguoc(self):
        if self.head is None or self.head.next is None:
            return
        
        stack = []
        current = self.head
        while current:
            stack.append(current)
            current = current.next
        
        self.head = stack.pop()
        current = self.head
        while stack:
            current.next = stack.pop()
            current = current.next
        current.next = None

    def InDanhSach(self):
        current = self.head
        while current:
            print(current.info, end=" ")
            current = current.next
        print()

dslk = DanhSachLienKet()
dslk.Them(1)
dslk.Them(2)
dslk.Them(3)
dslk.Them(4)

print("Danh sach truoc khi dao nguoc:")
dslk.InDanhSach()

dslk.DaoNguoc()

print("Danh sach sau khi dao nguoc:")
dslk.InDanhSach()
