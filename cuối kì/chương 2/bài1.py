def mang_DoiXung(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    # Kiểm tra nếu ma trận không phải là ma trận vuông
    if rows != cols:
        return False

    # Kiểm tra từng phần tử có phải là phần tử đối xứng hay không
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] != matrix[j][i]:
                return False
    return True

# Ví dụ ma trận đối xứng
example_matrix_symmetric = [
    [1, 2, 3],
    [2, 4, 5],
    [3, 5, 6]
]

# Ví dụ ma trận không đối xứng
example_matrix_not_symmetric = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Kiểm tra ma trận đối xứng:")
print("Ma trận đối xứng:", mang_DoiXung(example_matrix_symmetric))
print("Ma trận không đối xứng:", mang_DoiXung(example_matrix_not_symmetric))
