import copy

N, Q = map(int, input().split())


class Box:
    def __init__(self, index: int):
        self.index = index


class Pegion:
    def __init__(self, box: Box):
        self.box = box


boxes = [Box(i) for i in range(N)]
pegions = [Pegion(boxes[i]) for i in range(N)]

for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        a = q[1] - 1
        b = q[2] - 1
        pegion = pegions[a]
        box = boxes[b]
        pegion.box = box
    elif q[0] == 2:
        a = q[1] - 1
        b = q[2] - 1
        box_a = boxes[a]
        box_a_index = box_a.index
        box_b = boxes[b]
        box_b_index = box_b.index
        boxes[a] = box_b
        boxes[a].index = box_a_index
        boxes[b] = box_a
        boxes[b].index = box_b_index
    elif q[0] == 3:
        a = q[1] - 1
        print(pegions[a].box.index + 1)
