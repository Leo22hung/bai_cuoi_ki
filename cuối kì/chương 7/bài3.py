from collections import defaultdict

class DoThi:
    def __init__(self):
        self.graph = defaultdict(list)

    def ThemCanh(self, u, v):
        self.graph[u].append(v)

    def DFS(self, v, visited, parent):
        visited[v] = True
        for i in self.graph[v]:
            if not visited[i]:
                if self.DFS(i, visited, v):
                    return True
            elif parent != i:
                return True
        return False

    def ChuTrinh(self):
        V = len(self.graph)
        visited = [False] * V
        for v in range(V):
            if not visited[v]:
                if self.DFS(v, visited, -1):
                    return True
        return False

dt = DoThi()
dt.ThemCanh(0, 1)
dt.ThemCanh(1, 2)
dt.ThemCanh(2, 0)
if dt.ChuTrinh():
    print("Đồ thị có chu trình")
else:
    print("Đồ thị không có chu trình")
