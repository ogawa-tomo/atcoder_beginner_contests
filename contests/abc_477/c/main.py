from collections import defaultdict
import sys


class TIndexRange:
    def __init__(self, left: int, right: int) -> None:
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return str((self.left, self.right))


Q = int(input())
S = input()
T = input()

len_s = len(S)
len_t = len(T)

if len_t > len_s:
    for _ in range(Q):
        print("No")
    exit()

t_index_ranges: list[TIndexRange] = []
for i in range(len_s - len_t + 1):
    # print(S[i : i + len_t])
    if S[i : i + len_t] == T:
        t_index_ranges.append(TIndexRange(i, i + len_t - 1))

# print(t_index_ranges)
if not t_index_ranges:
    for _ in range(Q):
        print("No")
    exit()

# d[left]: leftが与えられたとき、Tを含む最小のright
d: defaultdict[int, int] = defaultdict(int)
index_range_index = 0
for left in range(len_s):
    index_range = t_index_ranges[index_range_index]
    while index_range_index < len(t_index_ranges) - 1 and index_range.left < left:
        index_range_index += 1
        index_range = t_index_ranges[index_range_index]

    if index_range.left < left:
        d[left] = sys.maxsize
    else:
        d[left] = index_range.right

# print(d)


for _ in range(Q):
    left, right = map(int, input().split())
    left -= 1
    right -= 1
    if d[left] <= right:
        print("Yes")
    else:
        print("No")
