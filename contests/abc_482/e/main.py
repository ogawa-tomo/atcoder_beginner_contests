# WA
from collections import deque
from itertools import combinations
import sys


sys.setrecursionlimit(10**9)  # 10^9が限界らしく、10^10にするとREになっちゃった


class Node:
    def __init__(self, i: int) -> None:
        self.i = i
        self.to_nodes: list[Node] = []
        self.distance: int | None = None  # スタートからの距離
        self.visited = False
        self.color = 0

    def __repr__(self) -> str:
        return str(i)


def bfs(start_node: Node):
    d: deque[Node] = deque()

    d.append(start_node)
    start_node.distance = 0
    while d:
        node = d.popleft()
        if node.distance is None:
            raise
        distance = node.distance
        for to_node in node.to_nodes:
            if to_node.distance is None:
                d.append(to_node)
                to_node.distance = distance + 1


class GetPath:
    def __init__(self, nodes: list[Node], start: Node, goal: Node) -> None:
        self.nodes = nodes
        self.start = start
        self.goal = goal
        self.path: list[Node] = []

    def dfs(self, node: Node):
        node.visited = True
        if node == self.goal:
            self.path.append(node)
            return True
        for to_node in node.to_nodes:
            if not to_node.visited and self.dfs(to_node):
                self.path.append(node)
                return True
        return False

    def get_path(self):
        if self.dfs(self.start):
            self.path.reverse()
            return self.path


def get_path(nodes: list[Node], start: Node, goal: Node):
    for node in nodes:
        node.visited = False
    gp = GetPath(nodes, start, goal)
    return gp.get_path()


N = int(input())

nodes = [Node(i) for i in range(N)]
for _ in range(N - 1):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    node_u = nodes[u]
    node_v = nodes[v]
    node_u.to_nodes.append(node_v)
    node_v.to_nodes.append(node_u)

bfs(nodes[0])
# for node in nodes:
#     print(node.distance)

farest_nodes: list[Node] = []
farest_node = nodes[0]
distance = 0
for node in nodes:
    if node.distance is None:
        raise
    if node.distance > distance:
        farest_node = node
        distance = node.distance
for node in nodes:
    if node.distance == distance:
        farest_nodes.append(node)
if len(farest_nodes) == 1:
    diameter = farest_nodes[0].distance
    farest_nodes.append(nodes[0])
else:
    path = get_path(nodes, farest_nodes[0], farest_nodes[1])
    if path is None:
        raise
    diameter = len(path) - 1


C = list(map(int, input().split()))
for i in range(N):
    c = C[i]
    nodes[i].color = c
# print(farest_nodes)
answer = 0
for node1, node2 in combinations(farest_nodes, 2):
    if node1.color != node2.color:
        continue
    answer += 1
print(answer)
