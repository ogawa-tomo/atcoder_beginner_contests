from typing import Union
import sys

sys.setrecursionlimit(1000000)

N, M = map(int, input().split())


class Node:
    def __init__(self) -> None:
        self.parent: Union[None, Node] = None
        self.size = 1

    def root(self):
        if self.parent is None:
            return self
        return self.parent.root()


class Link:
    def __init__(self, node_1: Node, node_2: Node):
        self.node_1 = node_1
        self.node_2 = node_2


nodes = [Node() for _ in range(N)]


def unite(link: Link):
    root_1 = link.node_1.root()
    root_2 = link.node_2.root()
    if root_1 == root_2:
        return
    if root_1.size < root_2.size:
        root_1.parent = root_2
        root_2.size += root_1.size
    else:
        root_2.parent = root_1
        root_1.size += root_2.size


def is_connected(node_1: Node, node_2: Node):
    return node_1.root() == node_2.root()


links: list[Link] = []
for _ in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    node_u = nodes[u]
    node_v = nodes[v]
    links.append(Link(node_u, node_v))

answer = 0
for link in links:
    node_1 = link.node_1
    node_2 = link.node_2
    # 親が同じだったら繋げちゃだめ
    if node_1.root() == node_2.root():
        answer += 1
        continue
    unite(link)
print(answer)
