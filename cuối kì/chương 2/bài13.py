def Nhan(a, b):
    # Hàm nhân hai số nguyên
    def multiply_arrays(arr1, arr2):
        len1, len2 = len(arr1), len(arr2)
        result = [0] * (len1 + len2)

        # Lặp qua từng chữ số của số arr1
        for i in range(len1):
            carry = 0

            # Lặp qua từng chữ số của số arr2
            for j in range(len2):
                temp = arr1[len1 - 1 - i] * arr2[len2 - 1 - j] + carry
                carry, temp = divmod(result[len1 + len2 - 1 - i - j] + temp, 10)
                result[len1 + len2 - 1 - i - j] = temp

            # Xử lý phần dư cuối cùng
            result[len1 + len2 - i - j - 1] += carry

        return result

    # Xác định phần dấu và phần số của a và b
    sign_a, number_a = a[0], a[1:]
    sign_b, number_b = b[0], b[1:]

    # Tính toán kết quả tạm thời
    temp_result = multiply_arrays(number_a, number_b)

    # Kiểm tra nếu cần thêm dấu âm vào kết quả tạm thời
    if sign_a != sign_b:
        temp_result = [9 - digit for digit in temp_result]

    # Kiểm tra nếu kết quả tạm thời tràn số
    if len(temp_result) > len(number_a) + len(number_b):
        return [-1] * (len(temp_result) + 1)  # Trả về mảng gồm các số -1 nếu kết quả bị tràn
    else:
        # Thêm phần dấu vào kết quả cuối cùng nếu cần
        if sign_a == 1 and sign_b == 0:
            return [1] + temp_result
        else:
            return [0] + temp_result

# Ví dụ
a = [0, 1, 2, 3]  # Số dương 123
b = [1, 4, 5, 6]  # Số âm -456
print("Kết quả của a * b:", Nhan(a, b))

c = [1, 9, 9, 9]  # Số âm -999
d = [0, 1, 0, 0]  # Số dương 100
print("Kết quả của c * d:", Nhan(c, d))
