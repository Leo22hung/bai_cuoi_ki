class HanoiTower:
    def __init__(self, num_disks):
        self.num_disks = num_disks
        self.tower1 = list(range(num_disks, 0, -1))  # Tạo tháp ban đầu ở vị trí 1
        self.tower2 = []
        self.tower3 = []
        
    def move_tower(self, n, source, target, auxiliary):
        if n == 1:
            disk = source.pop()
            target.append(disk)
            print("Di chuyen dia tu", source, "den", target)
        else:
            self.move_tower(n-1, source, auxiliary, target)
            self.move_tower(1, source, target, auxiliary)
            self.move_tower(n-1, auxiliary, target, source)

    def move(self):
        self.move_tower(self.num_disks, self.tower1, self.tower3, self.tower2)

num_disks = 3
hanoi_tower = HanoiTower(num_disks)
hanoi_tower.move()
