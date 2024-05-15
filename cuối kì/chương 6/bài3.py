def Giao(a, b):
    set_a = set(a)
    set_b = set(b)
    common_values = set_a.intersection(set_b)
    result = sorted(list(common_values))
    return result

a = [1, 5, 3, 7, 9, 4, 2]
b = [9, 6, 2, 3, 8]
result = Giao(a, b)
print("Mảng c chứa các số có trong cả mảng a và mảng b:", result)
