import sys
from typing import Union


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


nodes = [Node() for _ in range(N)]
for _ in range(M):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    root_A = nodes[A].root()
    root_B = nodes[B].root()
    if root_A == root_B:
        continue
    if root_A.size < root_B.size:
        root_A.parent = root_B
        root_B.size += root_A.size
    else:
        root_B.parent = root_A
        root_A.size += root_B.size
