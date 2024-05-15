def Cong(a, b):
    # Hàm tính tổng hai mảng số nguyên
    def sum_arrays(arr1, arr2):
        carry = 0
        result = []

        # Lặp qua từng cặp số từ phải sang trái
        while arr1 or arr2 or carry:
            num1 = arr1.pop() if arr1 else 0
            num2 = arr2.pop() if arr2 else 0
            total = num1 + num2 + carry
            carry = total // 10
            result.append(total % 10)

        # Đảo ngược kết quả để đảm bảo thứ tự đúng
        result.reverse()
        return result

    # Xác định phần dấu và phần số của a và b
    sign_a, number_a = a[0], a[1:]
    sign_b, number_b = b[0], b[1:]

    # Tính toán kết quả tạm thời
    temp_result = sum_arrays(number_a, number_b)

    # Kiểm tra nếu cần thêm dấu trừ vào kết quả tạm thời
    if sign_a == 1:
        temp_result = [9 - digit for digit in temp_result]

    # Kiểm tra nếu kết quả tạm thời tràn số
    if len(temp_result) > len(number_a):
        return [-1] * (len(temp_result) + 1)  # Trả về mảng gồm các số -1 nếu kết quả bị tràn
    else:
        # Thêm phần dấu vào kết quả cuối cùng nếu cần
        if sign_a == 1 and sign_b == 1:
            return [1] + temp_result
        else:
            return [0] + temp_result

# Ví dụ
a = [0, 1, 2, 3]  # Số dương 123
b = [1, 4, 5, 6]  # Số âm -456
print("Kết quả của a + b:", Cong(a, b))

c = [1, 9, 9, 9]  # Số âm -999
d = [0, 1, 0, 0]  # Số dương 100
print("Kết quả của c + d:", Cong(c, d))
def Cong(a, b):
    # Hàm tính tổng hai mảng số nguyên
    def sum_arrays(arr1, arr2):
        carry = 0
        result = []

        # Lặp qua từng cặp số từ phải sang trái
        while arr1 or arr2 or carry:
            num1 = arr1.pop() if arr1 else 0
            num2 = arr2.pop() if arr2 else 0
            total = num1 + num2 + carry
            carry = total // 10
            result.append(total % 10)

        # Đảo ngược kết quả để đảm bảo thứ tự đúng
        result.reverse()
        return result

    # Xác định phần dấu và phần số của a và b
    sign_a, number_a = a[0], a[1:]
    sign_b, number_b = b[0], b[1:]

    # Tính toán kết quả tạm thời
    temp_result = sum_arrays(number_a, number_b)

    # Kiểm tra nếu cần thêm dấu trừ vào kết quả tạm thời
    if sign_a == 1:
        temp_result = [9 - digit for digit in temp_result]

    # Kiểm tra nếu kết quả tạm thời tràn số
    if len(temp_result) > len(number_a):
        return [-1] * (len(temp_result) + 1)  # Trả về mảng gồm các số -1 nếu kết quả bị tràn
    else:
        # Thêm phần dấu vào kết quả cuối cùng nếu cần
        if sign_a == 1 and sign_b == 1:
            return [1] + temp_result
        else:
            return [0] + temp_result

# Ví dụ
a = [0, 1, 2, 3]  # Số dương 123
b = [1, 4, 5, 6]  # Số âm -456
print("Kết quả của a + b:", Cong(a, b))

c = [1, 9, 9, 9]  # Số âm -999
d = [0, 1, 0, 0]  # Số dương 100
print("Kết quả của c + d:", Cong(c, d))
def Cong(a, b):
    # Hàm tính tổng hai mảng số nguyên
    def sum_arrays(arr1, arr2):
        carry = 0
        result = []

        # Lặp qua từng cặp số từ phải sang trái
        while arr1 or arr2 or carry:
            num1 = arr1.pop() if arr1 else 0
            num2 = arr2.pop() if arr2 else 0
            total = num1 + num2 + carry
            carry = total // 10
            result.append(total % 10)

        # Đảo ngược kết quả để đảm bảo thứ tự đúng
        result.reverse()
        return result

    # Xác định phần dấu và phần số của a và b
    sign_a, number_a = a[0], a[1:]
    sign_b, number_b = b[0], b[1:]

    # Tính toán kết quả tạm thời
    temp_result = sum_arrays(number_a, number_b)

    # Kiểm tra nếu cần thêm dấu trừ vào kết quả tạm thời
    if sign_a == 1:
        temp_result = [9 - digit for digit in temp_result]

    # Kiểm tra nếu kết quả tạm thời tràn số
    if len(temp_result) > len(number_a):
        return [-1] * (len(temp_result) + 1)  # Trả về mảng gồm các số -1 nếu kết quả bị tràn
    else:
        # Thêm phần dấu vào kết quả cuối cùng nếu cần
        if sign_a == 1 and sign_b == 1:
            return [1] + temp_result
        else:
            return [0] + temp_result

# Ví dụ
a = [0, 1, 2, 3]  # Số dương 123
b = [1, 4, 5, 6]  # Số âm -456
print("Kết quả của a + b:", Cong(a, b))

c = [1, 9, 9, 9]  # Số âm -999
d = [0, 1, 0, 0]  # Số dương 100
print("Kết quả của c + d:", Cong(c, d))
