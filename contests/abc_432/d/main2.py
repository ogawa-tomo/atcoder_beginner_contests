from itertools import combinations
from collections import deque


class Block:
    def __init__(self, min_x: int, min_y: int, max_x: int, max_y: int):
        self.min_x = min_x
        self.min_y = min_y
        self.max_x = max_x
        self.max_y = max_y
        self.neighbors: list[Block] = []
        self.investigated = False

    def __repr__(self):
        return str([(self.min_x, self.min_y), (self.max_x, self.max_y)])

    def shift_y(self, y: int):
        self.min_y += y
        self.max_y += y

    def shift_x(self, x: int):
        self.min_x += x
        self.max_x += x

    def grid_num(self):
        return (self.max_x - self.min_x + 1) * (self.max_y - self.min_y + 1)


def is_renketsu(block1: Block, block2: Block):
    if block1.max_x + 1 == block2.min_x or block2.max_x + 1 == block1.min_x:
        return block1.min_y <= block2.max_y and block2.min_y <= block1.max_y
    if block1.max_y + 1 == block2.min_y or block2.max_y + 1 == block1.min_y:
        return block1.min_x <= block2.max_x and block2.min_x <= block1.max_x
    return False


N, X, Y = map(int, input().split())
blocks = [Block(0, 0, X - 1, Y - 1)]
for _ in range(N):
    query = input().split()
    a = int(query[1])
    b = int(query[2])
    new_blocks: list[Block] = []
    if query[0] == "X":
        for block in blocks:
            if a <= block.min_x:
                block.shift_y(b)
                new_blocks.append(block)
            elif block.max_x < a:
                block.shift_y(-b)
                new_blocks.append(block)
            else:
                left_block = Block(block.min_x, block.min_y, a - 1, block.max_y)
                right_block = Block(a, block.min_y, block.max_x, block.max_y)
                left_block.shift_y(-b)
                right_block.shift_y(b)
                new_blocks.append(left_block)
                new_blocks.append(right_block)

    elif query[0] == "Y":
        for block in blocks:
            if a <= block.min_y:
                block.shift_x(b)
                new_blocks.append(block)
            elif block.max_y < a:
                block.shift_x(-b)
                new_blocks.append(block)
            else:
                below_block = Block(block.min_x, block.min_y, block.max_x, a - 1)
                upper_block = Block(block.min_x, a, block.max_x, block.max_y)
                below_block.shift_x(-b)
                upper_block.shift_x(b)
                new_blocks.append(below_block)
                new_blocks.append(upper_block)
    blocks = new_blocks
    # print(blocks)

for pair in combinations(blocks, 2):
    block1 = pair[0]
    block2 = pair[1]
    # print(block1, block2)
    if is_renketsu(block1, block2):
        block1.neighbors.append(block2)
        block2.neighbors.append(block1)

renketsu_list: list[int] = []
for start_block in blocks:
    if start_block.investigated:
        continue
    d: deque[Block] = deque()
    start_block.investigated = True
    d.append(start_block)
    renketsu_num = 0
    while d:
        block = d.popleft()
        renketsu_num += block.grid_num()
        for neighbor in block.neighbors:
            if not neighbor.investigated:
                neighbor.investigated = True
                d.append(neighbor)
    renketsu_list.append(renketsu_num)

renketsu_list.sort()
print(len(renketsu_list))
print(*renketsu_list)
