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

    def Tich(self, dathuc2):
        result = DaThuc()  # Khởi tạo đa thức kết quả

        current1 = self.head
        while current1 is not None:
            current2 = dathuc2.head
            while current2 is not None:
                heso_moi = current1.heso * current2.heso
                somu_moi = current1.somu + current2.somu
                result.Them(heso_moi, somu_moi)
                current2 = current2.next
            current1 = current1.next

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
da_thuc1.Them(1, 1)
da_thuc1.Them(2, 0)

da_thuc2 = DaThuc()
da_thuc2.Them(2, 1)
da_thuc2.Them(1, 0)

print("Da thuc 1:")
da_thuc1.in_da_thuc()
print("Da thuc 2:")
da_thuc2.in_da_thuc()

da_thuc_tich = da_thuc1.Tich(da_thuc2)
print("Tich cua hai da thuc:")
da_thuc_tich.in_da_thuc()
