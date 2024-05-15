def DayConDauTien(a, b):
    # Tạo tập hợp chứa các dãy con của mảng a
    a_subsets = set()
    n = len(a)
    for i in range(n):
        for j in range(i, n):
            a_subsets.add(tuple(a[i:j+1]))

    # Tìm và trả về dãy con đầu tiên trong mảng b mà cũng có trong tập hợp dãy con của mảng a
    n = len(b)
    for i in range(n):
        for j in range(i, n):
            subset = tuple(b[i:j+1])
            if subset in a_subsets:
                return list(subset)
    return []

# Ví dụ
a = [1, 6, 2, 5, 3, 7, 9, 4, 2]
b = [9, 6, 2, 5, 3, 7, 8]
print("Dãy con đầu tiên có trong cả a và b:", DayConDauTien(a, b))
