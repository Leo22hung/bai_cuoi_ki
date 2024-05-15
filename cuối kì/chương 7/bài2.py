from collections import defaultdict

class DoThi:
    def __init__(self):
        self.graph = defaultdict(list)

    def ThemCanh(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def DFS(self, v, visited):
        visited[v] = True
        for i in self.graph[v]:
            if not visited[i]:
                self.DFS(i, visited)

    def SoThanhPhan(self):
        V = len(self.graph)
        visited = [False] * V
        count = 0
        for v in range(V):
            if not visited[v]:
                self.DFS(v, visited)
                count += 1
        return count

dt = DoThi()
dt.ThemCanh(0, 1)
dt.ThemCanh(0, 2)
dt.ThemCanh(1, 2)
dt.ThemCanh(3, 4)
print("Số thành phần liên thông:", dt.SoThanhPhan())
