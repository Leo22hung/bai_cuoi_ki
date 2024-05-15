def pascal_triangle(n):
    for line in range(0, n):
        for i in range(0, line + 1):
            print(binomial_coefficient(line, i), " ", end="")
        print()

def binomial_coefficient(n, k):
    res = 1
    if k > n - k:
        k = n - k
    for i in range(k):
        res *= (n - i)
        res //= (i + 1)
    return res

# Kiểm tra với số nguyên dương n nhập từ bàn phím
n = int(input("Nhập vào một số nguyên dương n: "))

if n <= 0:
    print("Vui lòng nhập số nguyên dương.")
else:
    print("Tam giác Pascal ứng với bậc", n, "là:")
    pascal_triangle(n)
