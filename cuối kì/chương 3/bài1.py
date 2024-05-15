class Node:
    def __init__(self, heso, somu):
        self.heso = heso
        self.somu = somu
        self.next = None

class DaThuc:
    def __init__(self):
        self.head = None

    def Them(self, heso, somu):
        if self.head is None:
            self.head = Node(heso, somu)
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = Node(heso, somu)

    def in_da_thuc(self):
        if self.head is None:
            print("Da thuc rong")
            return
        current = self.head
        while current is not None:
            print(f"{current.heso}*x^{current.somu}", end=" ")
            current = current.next
        print()

# Sử dụng
da_thuc = DaThuc()
da_thuc.Them(3, 2)
da_thuc.Them(5, 1)
da_thuc.Them(2, 0)
da_thuc.in_da_thuc()
