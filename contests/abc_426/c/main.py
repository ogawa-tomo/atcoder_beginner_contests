# TLE
import heapq

N, Q = map(int, input().split())

computers = [i for i in range(N)]
heapq.heapify(computers)

for _ in range(Q):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    count = 0
    # このループでO(N)かかるからだめ
    while True:
        version = computers[0]
        if version <= x:
            count += 1
            heapq.heappop(computers)
            heapq.heappush(computers, y)
        else:
            print(count)
            break
