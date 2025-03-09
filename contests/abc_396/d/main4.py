# DFSを使う解法
import sys

N, M = map(int, input().split())


class Node:
    def __init__(self, index: int) -> None:
        self.links: list[Link] = []
        self.visited = False
        self.index = index

    def __repr__(self):
        return str(self.index)


class Link:
    def __init__(self, label: int, to_node: Node):
        self.label = label
        self.to_node = to_node


nodes = [Node(i) for i in range(N)]


for _ in range(M):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    node_u = nodes[u]
    node_v = nodes[v]
    node_u.links.append(Link(w, node_v))
    node_v.links.append(Link(w, node_u))

answer = sys.maxsize


def dfs(node: Node, score: int):
    global answer

    node.visited = True

    if node.index == N - 1:
        answer = min(answer, score)

    for link in node.links:
        to_node = link.to_node
        if not to_node.visited:
            dfs(to_node, link.label ^ score)

    node.visited = False


dfs(nodes[0], 0)
print(answer)
