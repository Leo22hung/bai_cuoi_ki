def mang_NhomCot(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    # Tạo một từ điển để lưu trữ chỉ mục cột của các cột giống nhau
    groups = {}

    # Kiểm tra từng cặp cột trong ma trận
    for j in range(cols):
        col_content = tuple(matrix[i][j] for i in range(rows))  # Chuyển cột thành tuple để so sánh
        if col_content in groups:
            groups[col_content].append(j)  # Nếu cột đã xuất hiện, thêm chỉ mục cột vào nhóm
        else:
            groups[col_content] = [j]  # Nếu cột chưa xuất hiện, tạo một nhóm mới

    # In ra nhóm chỉ mục cột của các cột giống nhau
    for group in groups.values():
        print("Nhóm chỉ mục cột:", group)

# Ví dụ ma trận có các cột giống nhau
example_matrix_with_duplicate_columns = [
    [1, 2, 3],
    [4, 5, 4],
    [7, 8, 3]
]

print("In ra nhóm chỉ mục cột của các cột giống nhau:")
mang_NhomCot(example_matrix_with_duplicate_columns)
