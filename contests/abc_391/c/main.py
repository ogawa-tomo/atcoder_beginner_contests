N, Q = map(int, input().split())


class Pegion:
    def __init__(self, box_index: int):
        self.box_index = box_index


pegions = [Pegion(i) for i in range(N)]

# boxes[i]: i番目の箱にいる鳩の数
boxes = [1 for _ in range(N)]

# 複数の鳩がいるboxの数
num_many_pegions = 0

for _ in range(Q):
    query = list(input().split())
    if query[0] == "1":
        P = int(query[1])
        H = int(query[2])
        P -= 1
        H -= 1
        pegion = pegions[P]
        if boxes[pegion.box_index] == 2:
            num_many_pegions -= 1
        boxes[pegion.box_index] -= 1
        pegion.box_index = H
        boxes[pegion.box_index] += 1
        if boxes[pegion.box_index] == 2:
            num_many_pegions += 1

    elif query[0] == "2":
        print(num_many_pegions)
