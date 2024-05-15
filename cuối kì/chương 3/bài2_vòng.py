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

    def RutGon(self):
        if self.head is None:
            print("Da thuc rong")
            return

        current = self.head
        while True:
            temp = current.next
            while temp != self.head:
                if temp.somu == current.somu:
                    current.heso += temp.heso
                    prev.next = temp.next
                    temp = temp.next
                else:
                    prev = temp
                    temp = temp.next
            if current.heso == 0:
                if current == self.head:
                    self.head = current.next
                    if self.head == current:
                        self.head = None
                    current = self.head
                else:
                    prev.next = current.next
                    current = current.next
            else:
                prev = current
                current = current.next
            if current == self.head:
                break

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
da_thuc.Them(5, 1)
da_thuc.Them(2, 0)

print("Da thuc truoc khi rut gon:")
da_thuc.in_da_thuc()

da_thuc.RutGon()

print("Da thuc sau khi rut gon:")
da_thuc.in_da_thuc()
