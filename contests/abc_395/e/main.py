# これだと2/70でWA

import heapq
import sys

N, M, X = map(int, input().split())


max_distance = sys.maxsize
# max_distance = float("inf")
# print(max_distance)


class Node:
    def __init__(self) -> None:
        self.to_nodes: list[Node] = []
        self.from_nodes: list[Node] = []
        self.distance = max_distance
        self.finalized = False


class QueueObject:
    def __init__(self, node: Node, is_reversed: bool):
        self.node = node
        self.distance = node.distance
        self.is_reversed = is_reversed

    def __lt__(self, other):
        return self.distance < other.distance

    def __repr__(self):
        return str(self.distance)


nodes = [Node() for _ in range(N)]


for _ in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    node_u = nodes[u]
    node_v = nodes[v]
    node_u.to_nodes.append(node_v)
    node_v.from_nodes.append(node_u)

q: list[QueueObject] = []
nodes[0].distance = 0

heapq.heappush(q, QueueObject(nodes[0], False))
while q:
    queue_object = heapq.heappop(q)
    node = queue_object.node
    is_reversed = queue_object.is_reversed

    if node.finalized:
        continue
    node.finalized = True

    if not is_reversed:
        to_nodes = node.to_nodes
        from_nodes = node.from_nodes
    else:
        to_nodes = node.from_nodes
        from_nodes = node.to_nodes

    # 自分が向いているノード
    distance = node.distance + 1
    for to_node in to_nodes:
        if distance < to_node.distance:
            to_node.distance = distance
            heapq.heappush(q, QueueObject(to_node, is_reversed))
    # 自分に向いているノード
    distance = node.distance + X + 1
    for from_node in from_nodes:
        if distance < from_node.distance:
            from_node.distance = distance
            heapq.heappush(q, QueueObject(from_node, not is_reversed))

print(nodes[N - 1].distance)
