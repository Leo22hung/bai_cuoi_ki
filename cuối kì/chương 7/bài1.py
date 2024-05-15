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

    def LienThong(self):

        V = len(self.graph)
        visited = [False] * V
        self.DFS(list(self.graph.keys())[0], visited)
        for i in range(V):
            if not visited[i]:
                return False
        return True

dt = DoThi()
dt.ThemCanh(0, 1)
dt.ThemCanh(0, 2)
dt.ThemCanh(1, 2)
dt.ThemCanh(2, 3)
print("Đồ thị liên thông?:" , dt.LienThong())
