def factorial(num):
    if num == 0:
        return 1
    else:
        result = 1
        for i in range(1, num + 1):
            result *= i
        return result

def neper(n):
    if n < 0:
        return "Vui lòng nhập số nguyên không âm."
    else:
        e_sum = 0
        for k in range(n + 1):
            e_sum += 1 / factorial(k)
        return e_sum

# Kiểm tra với một số nguyên n nhập từ bàn phím
n = int(input("Nhập vào một số nguyên n >= 0: "))

print("Tổng của các số hạng a0 + a1 + ... + an của số Neper là:", neper(n))
