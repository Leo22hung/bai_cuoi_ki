def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

def fibonacci_iterative(n):
    if n <= 1:
        return n
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            c = a + b
            a, b = b, c
        return b

# Kiểm tra với một số nguyên n nhập từ bàn phím
n = int(input("Nhập vào một số nguyên n >= 0: "))

if n < 0:
    print("Vui lòng nhập số nguyên không âm.")
else:
    print("Sử dụng giải thuật đệ qui:")
    print("Fibonacci của", n, "là:", fibonacci_recursive(n))
    
    print("\nSử dụng giải thuật không đệ qui:")
    print("Fibonacci của", n, "là:", fibonacci_iterative(n))
