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
            new_node.next = self.head  # Tạo vòng liên kết đầu tiên
        else:
            current = self.head
            while current.next != self.head:  # Duyệt đến phần tử cuối cùng
                current = current.next
            current.next = new_node
            new_node.next = self.head  # Liên kết phần tử mới với phần tử đầu tiên để tạo vòng

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

    def Cong(self, dathuc2):
        result = DaThuc()
        current1 = self.head
        current2 = dathuc2.head
        while True:
            heso_moi = current1.heso + current2.heso
            somu_moi = current1.somu
            result.Them(heso_moi, somu_moi)
            current1 = current1.next
            current2 = current2.next
            if current1 == self.head and current2 == dathuc2.head:
                break

        result.RutGon()

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

da_thuc1 = DaThuc()
da_thuc1.Them(3, 2)
da_thuc1.Them(5, 1)
da_thuc1.Them(2, 0)

da_thuc2 = DaThuc()
da_thuc2.Them(2, 1)
da_thuc2.Them(1, 0)

print("Da thuc 1:")
da_thuc1.in_da_thuc()
print("Da thuc 2:")
da_thuc2.in_da_thuc()

da_thuc_tong = da_thuc1.Cong(da_thuc2)
print("Tong cua hai da thuc:")
da_thuc_tong.in_da_thuc()
