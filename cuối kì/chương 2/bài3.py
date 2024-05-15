def mang_TrungHang(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    # Kiểm tra từng cặp hàng trong ma trận
    for i in range(rows - 1):
        for j in range(i + 1, rows):
            # Nếu hai hàng giống nhau, trả về True
            if matrix[i] == matrix[j]:
                return True
    # Nếu không tìm thấy hai hàng giống nhau, trả về False
    return False

# Ví dụ ma trận có ít nhất hai hàng giống nhau
example_matrix_with_duplicate_rows = [
    [1, 2, 3],
    [4, 5, 6],
    [1, 2, 3]
]

# Ví dụ ma trận không có hai hàng giống nhau
example_matrix_without_duplicate_rows = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Kiểm tra ma trận có ít nhất hai hàng giống nhau:")
print("Ma trận có ít nhất hai hàng giống nhau:", mang_TrungHang(example_matrix_with_duplicate_rows))
print("Ma trận không có hai hàng giống nhau:", mang_TrungHang(example_matrix_without_duplicate_rows))
