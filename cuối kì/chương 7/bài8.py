from collections import defaultdict, deque

class DoThi:
    def __init__(self):
        self.graph = defaultdict(list)

    def ThemCungVoHuong(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def ThemCungHuUong(self, u, v):
        self.graph[u].append(v)

    def DuongDi(self, v1, v2):
        visited = set()
        queue = deque([v1])

        while queue:
            curr_vertex = queue.popleft()
            if curr_vertex == v2:
                return True
            visited.add(curr_vertex)
            for neighbor in self.graph[curr_vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)
        
        return False

dt = DoThi()
dt.ThemCungVoHuong(0, 1)
dt.ThemCungVoHuong(0, 2)
dt.ThemCungVoHuong(1, 2)
dt.ThemCungVoHuong(2, 3)

print("Có đường đi từ 0 đến 3:", dt.DuongDi(0, 3))
print("Có đường đi từ 2 đến 1:", dt.DuongDi(2, 1))
