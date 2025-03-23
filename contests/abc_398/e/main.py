N = int(input())


class Node:
    def __init__(self) -> None:
        self.neighbors: list[Node] = []


nodes = [Node() for _ in range(N)]

for _ in range(N - 1):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    node_u = nodes[u]
    node_v = nodes[v]
    node_u.neighbors.append(node_v)
    node_v.neighbors.append(node_u)
