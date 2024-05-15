def gcd_recursive(m, n):
    if n == 0:
        return m
    else:
        return gcd_recursive(n, m % n)

def gcd_iterative(m, n):
    while n != 0:
        m, n = n, m % n
    return m

# Kiểm tra với hai số nguyên dương m và n nhập từ bàn phím
m = int(input("Nhập số nguyên dương m: "))
n = int(input("Nhập số nguyên dương n: "))

if m <= 0 or n <= 0:
    print("Vui lòng nhập hai số nguyên dương.")
else:
    print("Sử dụng giải thuật đệ qui:")
    print("Ước số chung lớn nhất của", m, "và", n, "là:", gcd_recursive(m, n))

    print("\nSử dụng giải thuật không đệ qui:")
    print("Ước số chung lớn nhất của", m, "và", n, "là:", gcd_iterative(m, n))
