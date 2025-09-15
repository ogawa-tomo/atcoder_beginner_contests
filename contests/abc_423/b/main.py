N = int(input())
L = list(map(int, input().split()))

from_left = 1
for l in L:
    if l == 1:
        break
    from_left += 1

L.reverse()
# print(L)
from_right = 1
for l in L:
    if l == 1:
        break
    from_right += 1

print(max(N + 1 - from_left - from_right, 0))
