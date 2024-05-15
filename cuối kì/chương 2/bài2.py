def mang_TamGiacTren(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    # Kiểm tra nếu ma trận không phải là ma trận vuông
    if rows != cols:
        return False

    # Kiểm tra các phần tử nằm dưới đường chéo chính có bằng 0 không
    for i in range(rows):
        for j in range(i + 1, cols):
            if matrix[i][j] != 0:
                return False
    return True

# Ví dụ ma trận tam giác trên
example_matrix_upper_triangular = [
    [1, 2, 3],
    [0, 4, 5],
    [0, 0, 6]
]

# Ví dụ ma trận không phải tam giác trên
example_matrix_not_upper_triangular = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Kiểm tra ma trận tam giác trên:")
print("Ma trận tam giác trên:", mang_TamGiacTren(example_matrix_upper_triangular))
print("Ma trận không phải tam giác trên:", mang_TamGiacTren(example_matrix_not_upper_triangular))
