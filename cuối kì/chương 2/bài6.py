def Tru(a, b):
    # Chuyển a và b thành chuỗi
    a_str = ''.join(str(digit) for digit in a)
    b_str = ''.join(str(digit) for digit in b)

    # Chuyển chuỗi thành số nguyên và thực hiện phép trừ
    result = int(a_str) - int(b_str)

    return result

# Ví dụ
a = [3, 2, 1]
b = [1, 2, 1]
print("Kết quả của a - b:", Tru(a, b))

c = [5, 0, 0]
d = [2, 5, 0]
print("Kết quả của c - d:", Tru(c, d))
