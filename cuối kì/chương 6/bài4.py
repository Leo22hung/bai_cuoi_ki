def Hop(a, b):
    set_a = set(a)
    set_b = set(b)
    union_values = set_a.union(set_b)
    result = sorted(list(union_values))
    return result

a = [1, 5, 3, 7, 9, 4, 2]
b = [9, 6, 2, 3, 8]
result = Hop(a, b)
print("Mảng c chứa các số có trong mảng a hoặc mảng b:", result)
