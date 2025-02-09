import sys
from typing import Union


N, M = map(int, input().split())


class Server:
    def __init__(self) -> None:
        self.group_index: Union[None, int] = None


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
    # すでに同じグループの場合
    if server1.group_index is not None and server1.group_index == server2.group_index:
        # 余計なケーブル
        continue

    # 両方とも未所属の場合
    if server1.group_index is None and server2.group_index is None:
        group_index = len(server_groups)
        server1.group_index = group_index
        server2.group_index = group_index
        server_groups.append([server1, server2])
        continue

    # サーバー1️が未所属の場合
    if server1.group_index is None:
        server1.group_index = server2.group_index
        server_groups[server2.group_index].append(server1)
        continue
    if server2.group_index is None:
        server2.group_index = server1.group_index
        server_groups[server1.group_index].append(server2)
        continue

    # ともに所属先がある場合
