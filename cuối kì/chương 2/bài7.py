def Nhan(a, b):
    # Chuyển a và b thành chuỗi
    a_str = ''.join(str(digit) for digit in a)
    b_str = ''.join(str(digit) for digit in b)

    # Thực hiện phép nhân
    result = int(a_str) * int(b_str)

    # Kiểm tra tràn số
    if result > 99999999:  # Kiểm tra xem kết quả có lớn hơn 99,999,999 không
        return [-1]  # Trả về mảng gồm số -1 nếu kết quả bị tràn
    else:
        return [int(digit) for digit in str(result)]  # Trả về kết quả dưới dạng mảng

# Ví dụ
a = [1, 2, 3]
b = [4, 5, 6]
print("Kết quả của a * b:", Nhan(a, b))

c = [9, 9, 9]
d = [1, 0, 0]
print("Kết quả của c * d:", Nhan(c, d))
