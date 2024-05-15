from collections import defaultdict

class DoThi:
    def __init__(self):
        self.graph = defaultdict(list)

    def ThemCanh(self, u, v):
        self.graph[u].append(v)

    def ChuaDinh(self, v):
        return v in self.graph

dt = DoThi()
dt.ThemCanh(0, 1)
dt.ThemCanh(1, 2)
if dt.ChuaDinh(1):
    print("Đỉnh 1 tồn tại trong đồ thị")
else:
    print("Đỉnh 1 không tồn tại trong đồ thị")
