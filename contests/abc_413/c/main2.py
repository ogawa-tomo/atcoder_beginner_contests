from collections import deque

Q = int(input())
A: list[int] = []


class NumSet:
    def __init__(self, num: int, value: int):
        self.num = num
        self.value = value

    def __repr__(self):
        return f"[{self.value}, {self.num}]"


queue: deque[NumSet] = deque()
current_index = 0
for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        c = q[1]
        x = q[2]
        queue.append(NumSet(c, x))
    elif q[0] == 2:
        k = q[1]
        answer = 0
        while queue and queue[0].num <= k:
            answer += queue[0].num * queue[0].value
            k -= queue[0].num
            queue.popleft()
        if k != 0:
            queue[0].num -= k
            answer += k * queue[0].value
        print(answer)
