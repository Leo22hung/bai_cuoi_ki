def Cong(a, b):
    # Kiểm tra độ dài của a và b
    len_a = len(a)
    len_b = len(b)

    # Tính độ dài của số lớn hơn trong hai số
    max_len = max(len_a, len_b)

    # Chuyển a và b thành chuỗi và đảm bảo chúng có cùng độ dài
    a_str = ''.join(str(digit) for digit in a).zfill(max_len)
    b_str = ''.join(str(digit) for digit in b).zfill(max_len)

    # Thực hiện phép cộng
    result = int(a_str) + int(b_str)

    # Kiểm tra tràn số
    if result > 99999999:  # Kiểm tra xem kết quả có lớn hơn 99,999,999 không
        return [-1] * max_len  # Trả về mảng gồm các số -1 nếu kết quả bị tràn
    else:
        return [int(digit) for digit in str(result).zfill(max_len)]  # Trả về kết quả dưới dạng mảng

# Ví dụ
a = [1, 2, 3]
b = [4, 5, 6]
print("Kết quả của a + b:", Cong(a, b))

c = [9, 9, 9]
d = [1, 0, 0]
print("Kết quả của c + d:", Cong(c, d))
