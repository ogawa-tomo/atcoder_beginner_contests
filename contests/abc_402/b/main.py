from collections import deque

Q = int(input())


queue: deque[int] = deque()

for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        queue.append(query[1])
    else:
        print(queue.popleft())
