import sys
from typing import Union


N, M = map(int, input().split())


class Server:
    def __init__(self) -> None:
        self.parent: Union[None, Server] = None
        self.size = 1

    def root(self):
        if self.parent is None:
            return self
        return self.parent.root()

    def single(self):
        return self.size == 1


class Cable:
    def __init__(self, left: Server, right: Server):
        self.left = left
        self.right = right


servers = [Server() for _ in range(N)]
cables: list[Cable] = []
server_groups: list[list[Server]] = []
for _ in range(M):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    server1 = servers[A]
    server2 = servers[B]
    cable = Cable(server1, server2)
    cables.append(cable)
    root1 = server1.root()
    root2 = server2.root()
    # すでに同じグループの場合
    if root1 == root2:
        # 余計なケーブルを記録
        continue
