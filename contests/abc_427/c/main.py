import sys

N, M = map(int, input().split())


class Node:
    def __init__(self) -> None:
        self.neighbors: list[Node] = []
        self.color = "white"  # white or black


nodes = [Node() for _ in range(N)]
for _ in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    nodes[u].neighbors.append(nodes[v])
    nodes[v].neighbors.append(nodes[u])


answer = sys.maxsize
for i in range(1 << N):
    white_nodes: list[Node] = []
    black_nodes: list[Node] = []
    for k in range(N):
        node = nodes[k]
        if i >> k & 1:
            node.color = "black"
            black_nodes.append(node)
        else:
            node.color = "white"
            white_nodes.append(node)
    tmp_answer = 0
    for node in white_nodes:
        for neighbor in node.neighbors:
            if neighbor.color == "white":
                tmp_answer += 1
                # neighbor.neighbors.remove(node)
    for node in black_nodes:
        for neighbor in node.neighbors:
            if neighbor.color == "black":
                tmp_answer += 1
                # neighbor.neighbors.remove(node)
    tmp_answer //= 2
    answer = min(answer, tmp_answer)
print(answer)
