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

    def Chep(self):
        result = DaThuc()  # Khởi tạo đa thức kết quả

        current = self.head
        while current is not None:
            result.Them(current.heso, current.somu)
            current = current.next

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

# Sử dụng
da_thuc = DaThuc()
da_thuc.Them(3, 2)
da_thuc.Them(5, 1)
da_thuc.Them(2, 0)

print("Da thuc goc:")
da_thuc.in_da_thuc()

da_thuc_copy = da_thuc.Chep()
print("Da thuc sao chep:")
da_thuc_copy.in_da_thuc()
