# WA/TLE
from itertools import combinations
from collections import deque


class Grid:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __repr__(self):
        return str((self.x, self.y))


class Block:
    def __init__(self, lower_left: Grid, upper_right: Grid):
        self.lower_left = lower_left
        self.upper_right = upper_right
        self.neighbors: list[Block] = []
        self.investigated = False

    def __repr__(self):
        return str([self.lower_left, self.upper_right])

    def left_x(self):
        return self.lower_left.x

    def right_x(self):
        return self.upper_right.x

    def shift_y(self, y: int):
        self.lower_left.y += y
        self.upper_right.y += y

    def below_y(self):
        return self.lower_left.y

    def above_y(self):
        return self.upper_right.y

    def shift_x(self, x: int):
        self.lower_left.x += x
        self.upper_right.x += x

    def grid_num(self):
        return (self.right_x() - self.left_x() + 1) * (
            self.above_y() - self.below_y() + 1
        )


def is_renketsu(block1: Block, block2: Block):
    if (
        block1.right_x() + 1 == block2.left_x()
        or block2.right_x() + 1 == block1.left_x()
    ):
        return (
            block1.below_y() <= block2.above_y()
            and block2.below_y() <= block1.above_y()
        )
    if (
        block1.above_y() + 1 == block2.below_y()
        or block2.above_y() + 1 == block1.below_y()
    ):
        return (
            block1.left_x() <= block2.right_x() and block2.left_x() <= block1.right_x()
        )
    return False


N, X, Y = map(int, input().split())
blocks = [Block(Grid(0, 0), Grid(X - 1, Y - 1))]
for _ in range(N):
    query = input().split()
    a = int(query[1])
    b = int(query[2])
    new_blocks: list[Block] = []
    if query[0] == "X":
        for block in blocks:
            if a <= block.left_x():
                block.shift_y(b)
                new_blocks.append(block)
            elif block.right_x() < a:
                block.shift_y(-b)
                new_blocks.append(block)
            else:
                left_block = Block(
                    Grid(block.lower_left.x, block.lower_left.y),
                    Grid(a - 1, block.upper_right.y),
                )
                right_block = Block(
                    Grid(a, block.lower_left.y),
                    Grid(block.upper_right.x, block.upper_right.y),
                )
                left_block.shift_y(-b)
                right_block.shift_y(b)
                new_blocks.append(left_block)
                new_blocks.append(right_block)

    elif query[0] == "Y":
        for block in blocks:
            if a <= block.below_y():
                block.shift_x(b)
                new_blocks.append(block)
            elif block.above_y() < a:
                block.shift_x(-b)
                new_blocks.append(block)
            else:
                below_block = Block(
                    Grid(block.lower_left.x, block.lower_left.y),
                    Grid(block.upper_right.x, a - 1),
                )
                upper_block = Block(
                    Grid(block.lower_left.x, a),
                    Grid(block.upper_right.x, block.upper_right.y),
                )
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
    d.append(start_block)
    renketsu_num = 0
    while d:
        block = d.popleft()
        block.investigated = True
        renketsu_num += block.grid_num()
        for neighbor in block.neighbors:
            if not neighbor.investigated:
                # ここでinvestigatedフラグをTrueにしないのが間違い。ここでTrueにしておかないと、二重カウントになりうる。
                d.append(neighbor)
    renketsu_list.append(renketsu_num)

renketsu_list.sort()
print(len(renketsu_list))
print(*renketsu_list)


# renketsu_list: list[int] = []
# # for i in range(len(blocks) - 1):
# i = 0
# while i < len(blocks) - 1:
#     block = blocks[i]
#     next_block = blocks[i + 1]
#     if is_renketsu(block, next_block):
#         renketsu_list.append(block.grid_num() + next_block.grid_num())
#         i += 2
#     else:
#         renketsu_list.append(block.grid_num())
#         i += 1
# renketsu_list.sort()
# print(len(renketsu_list))
# print(*renketsu_list)
