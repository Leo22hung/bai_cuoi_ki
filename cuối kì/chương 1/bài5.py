def classify_number(n):
    sum_of_divisors = sum([i for i in range(1, n) if n % i == 0])
    if sum_of_divisors < n:
        return "deficient"
    elif sum_of_divisors == n:
        return "perfect"
    else:
        return "abundant"

def numbers_classification(x, y):
    if x <= 0 or y <= 0 or x > y:
        print("Vui lòng nhập hai số nguyên dương hợp lệ với x ≤ y.")
    else:
        print("Phân loại các số từ", x, "đến", y, "là:")
        for num in range(x, y + 1):
            print("Số", num, "là", classify_number(num))

# Kiểm tra với hai số nguyên dương x và y nhập từ bàn phím
x = int(input("Nhập vào số nguyên dương x: "))
y = int(input("Nhập vào số nguyên dương y (x ≤ y): "))

numbers_classification(x, y)
