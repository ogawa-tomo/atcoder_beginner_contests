# 途中
from collections import deque


class Node:
    def __init__(self, i: int) -> None:
        self.i = i
        self.links: list[Link] = []
        # self.


class Link:
    def __init__(self, cost: int, to_node: Node):
        self.cost = cost
        self.to_node = to_node


N, M, L, S, T = map(int, input().split())
nodes = [Node(i) for i in range(N)]
for _ in range(M):
    u, v, c = map(int, input().split())
    u -= 1
    v -= 1
    from_node = nodes[u]
    to_node = nodes[v]
    from_node.links.append(Link(c, to_node))

d: deque[Node] = deque()
d.append(nodes[0])
# nodes[0].distance = 0
