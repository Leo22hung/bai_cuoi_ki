def mang_Dao(matrix):
    # Hàm tính diện tích lớn nhất của các đảo hình chữ nhật trong ma trận
    def max_rectangle_area(matrix):
        if not matrix:
            return 0

        m, n = len(matrix), len(matrix[0])
        heights = [0] * n
        max_area = 0

        for i in range(m):
            for j in range(n):
                heights[j] = heights[j] + 1 if matrix[i][j] == 1 else 0

            max_area = max(max_area, largest_rectangle_area(heights))

        return max_area

    # Hàm tính diện tích lớn nhất của hình chữ nhật
    def largest_rectangle_area(heights):
        stack = []
        max_area = 0
        heights.append(0)

        for i, height in enumerate(heights):
            while stack and heights[stack[-1]] >= height:
                h = heights[stack.pop()]
                w = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, h * w)

            stack.append(i)

        return max_area

    return max_rectangle_area(matrix)

# Ví dụ
mang = [
    [1, 0, 1, 1, 0],
    [1, 0, 1, 1, 1],
    [0, 1, 1, 1, 1],
    [0, 1, 0, 1, 0]
]

print("Diện tích lớn nhất của các đảo hình chữ nhật trong ma trận:")
print(mang_Dao(mang))
