import sys

sys.setrecursionlimit(10**9)

N, M = map(int, input().split())


class Node:
    def __init__(self, i: int):
        self.i = i
        self.from_nodes: list[Node] = []
        self.to_nodes: list[Node] = []
        self.to_black = False

    def __repr__(self):
        return str(self.i)


nodes = [Node(i) for i in range(N)]
for _ in range(M):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    # nodes[x].to_nodes.append(nodes[y])
    nodes[y].from_nodes.append(nodes[x])


def dfs(node: Node):
    node.to_black = True
    for from_node in node.from_nodes:
        if not from_node.to_black:
            dfs(from_node)


Q = int(input())

for _ in range(Q):
    x, v = map(int, input().split())
    v -= 1
    node = nodes[v]
    if x == 1:
        if not node.to_black:
            dfs(node)
    elif x == 2:
        if node.to_black:
            print("Yes")
        else:
            print("No")
