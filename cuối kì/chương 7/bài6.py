from collections import defaultdict

class DoThi:
    def __init__(self):
        self.graph = defaultdict(list)

    def ThemCung(self, u, v):
        self.graph[u].append(v)

    def SoCungVao(self, v):
        count = 0
        for node in self.graph:
            for neighbor in self.graph[node]:
                if neighbor == v:
                    count += 1
        return count

dt = DoThi()
dt.ThemCung(0, 1)
dt.ThemCung(0, 2)
dt.ThemCung(1, 2)
dt.ThemCung(2, 0)
dt.ThemCung(2, 3)
print("Số cung vào đỉnh 0:", dt.SoCungVao(0))
print("Số cung vào đỉnh 1:", dt.SoCungVao(1))
print("Số cung vào đỉnh 2:", dt.SoCungVao(2))
print("Số cung vào đỉnh 3:", dt.SoCungVao(3))
