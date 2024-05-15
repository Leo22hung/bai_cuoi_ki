def DayConDaiNhat(a, b):
    # Hàm tìm dãy con có chiều dài lớn nhất trong a và b
    def longest_common_subarray(a, b):
        len_a, len_b = len(a), len(b)
        dp = [[0] * (len_b + 1) for _ in range(len_a + 1)]
        max_len, end_index = 0, 0

        for i in range(1, len_a + 1):
            for j in range(1, len_b + 1):
                if a[i - 1] == b[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    if dp[i][j] > max_len:
                        max_len = dp[i][j]
                        end_index = i - 1

        return a[end_index - max_len + 1:end_index + 1]

    return longest_common_subarray(a, b)

# Ví dụ
a = [1, 6, 2, 5, 3, 7, 9, 4, 2, 8, 1, 5]
b = [6, 2, 5, 3, 7, 9, 8, 1, 5]
print("Dãy con dài nhất có trong cả a và b:", DayConDaiNhat(a, b))
