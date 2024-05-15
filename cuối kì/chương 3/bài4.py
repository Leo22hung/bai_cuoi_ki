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

    def RutGon(self):
        if self.head is None:
            print("Da thuc rong")
            return

        current = self.head
        while current is not None:
            temp = current
            while temp.next is not None:
                if temp.next.somu == current.somu:
                    current.heso += temp.next.heso
                    temp.next = temp.next.next
                else:
                    temp = temp.next
            if current.heso == 0:
                if current == self.head:
                    self.head = current.next
                    current = self.head
                else:
                    temp.next = current.next
                    current = current.next
            else:
                current = current.next

    def DoiDau(self):
        current = self.head
        while current is not None:
            current.heso = -current.heso  # Đảo dấu của hệ số
            current = current.next

    def in_da_thuc(self):
        if self.head is None:
            print("Da thuc rong")
            return
        current = self.head
        while current is not None:
            print(f"{current.heso}*x^{current.somu}", end=" ")
            current = current.next
        print()

da_thuc = DaThuc()
da_thuc.Them(3, 2)
da_thuc.Them(-5, 1)
da_thuc.Them(2, 0)

print("Da thuc truoc khi doi dau:")
da_thuc.in_da_thuc()

da_thuc.DoiDau()

print("Da thuc sau khi doi dau:")
da_thuc.in_da_thuc()
