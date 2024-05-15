def mang_TamGiacDuoi(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    # Kiểm tra nếu ma trận không phải là ma trận vuông
    if rows != cols:
        return False

    # Kiểm tra các phần tử nằm trên đường chéo chính và bên trên đường chéo chính
    for i in range(rows):
        for j in range(i + 1):
            if matrix[i][j] != 0:
                return False
    return True

# Ví dụ ma trận tam giác dưới
example_matrix_lower_triangular = [
    [1, 0, 0],
    [2, 3, 0],
    [4, 5, 6]
]

# Ví dụ ma trận không phải tam giác dưới
example_matrix_not_lower_triangular = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Kiểm tra ma trận tam giác dưới:")
print("Ma trận tam giác dưới:", mang_TamGiacDuoi(example_matrix_lower_triangular))
print("Ma trận không phải tam giác dưới:", mang_TamGiacDuoi(example_matrix_not_lower_triangular))
