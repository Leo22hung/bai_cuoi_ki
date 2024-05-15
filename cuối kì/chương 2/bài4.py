def mang_NhomHang(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    # Tạo một từ điển để lưu trữ chỉ mục hàng của các hàng giống nhau
    groups = {}

    # Kiểm tra từng hàng trong ma trận
    for i in range(rows):
        row_content = tuple(matrix[i])  # Chuyển hàng thành tuple để so sánh
        if row_content in groups:
            groups[row_content].append(i)  # Nếu hàng đã xuất hiện, thêm chỉ mục hàng vào nhóm
        else:
            groups[row_content] = [i]  # Nếu hàng chưa xuất hiện, tạo một nhóm mới

    # In ra nhóm chỉ mục hàng của các hàng giống nhau
    for group in groups.values():
        print("Nhóm chỉ mục hàng:", group)

# Ví dụ ma trận có các hàng giống nhau
example_matrix_with_duplicate_rows = [
    [1, 2, 3],
    [4, 5, 6],
    [1, 2, 3]
]

print("In ra nhóm chỉ mục hàng của các hàng giống nhau:")
mang_NhomHang(example_matrix_with_duplicate_rows)
