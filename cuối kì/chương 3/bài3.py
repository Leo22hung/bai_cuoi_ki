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

    def Cong(self, dathuc2):
        result = DaThuc()
        current1 = self.head
        current2 = dathuc2.head

        while current1 is not None and current2 is not None:
            if current1.somu > current2.somu:
                result.Them(current1.heso, current1.somu)
                current1 = current1.next
            elif current1.somu < current2.somu:
                result.Them(current2.heso, current2.somu)
                current2 = current2.next
            else:
                result.Them(current1.heso + current2.heso, current1.somu)
                current1 = current1.next
                current2 = current2.next

        while current1 is not None:
            result.Them(current1.heso, current1.somu)
            current1 = current1.next

        while current2 is not None:
            result.Them(current2.heso, current2.somu)
            current2 = current2.next

        result.RutGon()
        return result

    def in_da_thuc(self):
        if self.head is None:
            print("Da thuc rong")
            return
        current = self.head
        while current is not None:
            print(f"{current.heso}*x^{current.somu}", end=" ")
            current = current.next
        print()

da_thuc1 = DaThuc()
da_thuc1.Them(3, 2)
da_thuc1.Them(5, 1)
da_thuc1.Them(2, 0)

da_thuc2 = DaThuc()
da_thuc2.Them(2, 3)
da_thuc2.Them(1, 1)
da_thuc2.Them(2, 0)

print("Da thuc 1:")
da_thuc1.in_da_thuc()
print("Da thuc 2:")
da_thuc2.in_da_thuc()

da_thuc_tong = da_thuc1.Cong(da_thuc2)
print("Tong cua hai da thuc:")
da_thuc_tong.in_da_thuc()
