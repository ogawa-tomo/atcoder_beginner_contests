import heapq


class Battery:
    def __init__(self, charge: int):
        self.charge = charge

    def __lt__(self, other):
        # 逆
        return self.charge > other.charge

    def __repr__(self):
        return str(self.charge)


Q, V = map(int, input().split())

q: list[Battery] = []
actual_time = 0
virtual_time = 0
for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        t = query[1]
        w = query[2]

        actual_time = t
        virtual_time = -t

        battery = Battery(virtual_time + w)
        heapq.heappush(q, battery)
    elif query[0] == 2:
        t = query[1]

        actual_time = t
        virtual_time = -t

        if q:
            battery = heapq.heappop(q)
            charge = battery.charge - virtual_time
            print(min(charge, V))
        else:
            print(-1)
