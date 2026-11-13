from collections import deque

N = int(input())
S = input()

q: deque[int] = deque()
from_right = True
for i in range(N):
    n = i + 1
    s = S[i]

    if from_right:
        q.append(n)
    else:
        q.appendleft(n)

    # xのときは、
    if s == "o":
        from_right = not from_right

if not from_right:
    q.reverse()

print(*q)
