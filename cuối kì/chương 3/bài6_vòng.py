class Node:
    def __init__(self, heso, somu):
        self.heso = heso
        self.somu = somu
        self.next = None

class DaThuc:
    def __init__(self):
        self.head = None

    def Them(self, heso, somu):
        new_node = Node(heso, somu)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head
    def Chep(self):
        if self.head is None:
            print("Da thuc rong")
            return None

        result = DaThuc()

        current = self.head
        while True:
            result.Them(current.heso, current.somu)
            current = current.next
            if current == self.head:
                break

        return result

    def in_da_thuc(self):
        if self.head is None:
            print("Da thuc rong")
            return
        current = self.head
        while True:
            print(f"{current.heso}*x^{current.somu}", end=" ")
            current = current.next
            if current == self.head:
                break
        print()

da_thuc = DaThuc()
da_thuc.Them(3, 2)
da_thuc.Them(-5, 1)
da_thuc.Them(2, 0)

print("Da thuc ban dau:")
da_thuc.in_da_thuc()

da_thuc_copy = da_thuc.Chep()

print("Sao chep cua da thuc:")
da_thuc_copy.in_da_thuc()
