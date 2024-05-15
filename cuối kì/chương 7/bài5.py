from collections import defaultdict

class DoThi:
    def __init__(self):
        self.graph = defaultdict(list)

    def ThemCanh(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def BacDinh(self, v):
        return len(self.graph[v])

dt = DoThi()
dt.ThemCanh(0, 1)
dt.ThemCanh(0, 2)
dt.ThemCanh(1, 3)
print("Bậc của đỉnh 0:", dt.BacDinh(0))
print("Bậc của đỉnh 1:", dt.BacDinh(1))
print("Bậc của đỉnh 2:", dt.BacDinh(2))
print("Bậc của đỉnh 3:", dt.BacDinh(3))
