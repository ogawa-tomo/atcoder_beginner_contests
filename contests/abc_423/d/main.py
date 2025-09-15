import heapq

N, K = map(int, input().split())


class Group:
    def __init__(self, arrival_time: int, stay_time: int, num: int):
        self.arrival_time = arrival_time
        self.stay_time = stay_time
        self.num = num
        self.out_time = 0

    def __lt__(self, other):
        return self.out_time < other.out_time


groups: list[Group] = []
for _ in range(N):
    a, b, c = map(int, input().split())
    group = Group(a, b, c)
    groups.append(group)

groups_in_restaurant: list[Group] = []
current_time = 0
total = 0
for group in groups:
    if current_time < group.arrival_time:
        current_time = group.arrival_time
    while groups_in_restaurant and groups_in_restaurant[0].out_time < current_time:
        out_group = heapq.heappop(groups_in_restaurant)
        total -= out_group.num
    while total + group.num > K:
        out_group = heapq.heappop(groups_in_restaurant)
        current_time = out_group.out_time
        total -= out_group.num
    print(current_time)
    total += group.num
    group.out_time = current_time + group.stay_time
    heapq.heappush(groups_in_restaurant, group)
