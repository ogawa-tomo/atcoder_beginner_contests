from typing import Union

N, W = map(int, input().split())


class Block:
    def __init__(self, x: int, y: int, index: int):
        self.x = x
        self.y = y
        self.index = index

    def __repr__(self):
        return str(self.index)


blocks: list[Block] = []
columns: list[list[Block]] = []
for _ in range(W):
    columns.append([])

for i in range(N):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    block = Block(x, y, i)
    blocks.append(block)
    columns[x].append(block)
# print(columns)
for column in columns:
    column.sort(key=lambda block: block.y)
# print(columns)

Q = int(input())
for _ in range(Q):
    T, A = map(int, input().split())
    A -= 1
    block = blocks[A]

    # このブロックは、自分のいるカラムでn番目→二分探索
    # ok番目のy座標がこのブロックのy座標以下であるような最大のokを求める
    column = columns[block.x]
    ok = -1
    ng = len(column)
    while ng - ok > 1:
        mid = (ok + ng) // 2
        if column[mid].y <= block.y:
            ok = mid
        else:
            ng = mid
    n = ok
    # print(column)
    # print(n)

    # n番目のブロックのうち、一番上の座標→二分探索
    n_blocks = []
    n_blocks_exists = True
    for column in columns:
        if len(column) <= n:
            n_blocks_exists = False
            break
    if not n_blocks_exists:
        print("Yes")
        continue

    n_blocks = [column[n] for column in columns]
    max_y = max([block.y for block in n_blocks])
    deleted_time = max_y + 1
    target_time = T + 0.5
    if target_time < deleted_time:
        print("Yes")
    else:
        print("No")
