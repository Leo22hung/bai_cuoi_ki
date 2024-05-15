from collections import defaultdict

class DoThi:
    def __init__(self):
        self.graph = defaultdict(list)

    def ThemCung(self, u, v):
        self.graph[u].append(v)

    def SoCungRa(self, v):
        return len(self.graph[v])

dt = DoThi()
dt.ThemCung(0, 1)
dt.ThemCung(0, 2)
dt.ThemCung(1, 2)
dt.ThemCung(2, 0)
dt.ThemCung(2, 3)
print("Số cung ra từ đỉnh 0:", dt.SoCungRa(0))
print("Số cung ra từ đỉnh 1:", dt.SoCungRa(1))
print("Số cung ra từ đỉnh 2:", dt.SoCungRa(2))
print("Số cung ra từ đỉnh 3:", dt.SoCungRa(3))
