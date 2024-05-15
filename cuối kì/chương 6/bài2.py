def Hieu(a, b):
    set_a = set(a)
    set_b = set(b)
    unique_values = set_a.difference(set_b)
    result = sorted(list(unique_values))
    return result

a = [1, 5, 3, 7, 9, 4, 2]
b = [9, 6, 2, 3, 8]
result = Hieu(a, b)
print("Mảng c chứa các số không trùng nhau có trong mảng a và không có trong mảng b:", result)
