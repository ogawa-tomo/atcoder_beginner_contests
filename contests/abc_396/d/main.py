# ダイクストラ法だが、これは誤り
import heapq
import sys

max_distance = sys.maxsize

N, M = map(int, input().split())


class Node:
    def __init__(self) -> None:
        self.links: list[Link] = []
        self.distance = max_distance
        self.finalized = False


class Link:
    def __init__(self, distance: int, to_node: Node):
        self.distance = distance
        self.to_node = to_node


class QueueObject:
    def __init__(self, node: Node):
        self.node = node
        self.distance = node.distance

    def __lt__(self, other):
        return self.distance < other.distance

    def __repr__(self):
        return str(self.distance)


nodes = [Node() for _ in range(N)]

for _ in range(M):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    node_u = nodes[u]
    node_v = nodes[v]
    node_u.links.append(Link(w, node_v))
    node_v.links.append(Link(w, node_u))

q: list[QueueObject] = []
nodes[0].distance = 0

heapq.heappush(q, QueueObject(nodes[0]))
while q:
    queue_object = heapq.heappop(q)
    node = queue_object.node

    if node.finalized:
        continue
    node.finalized = True

    for link in node.links:
        distance = node.distance ^ link.distance
        if distance < link.to_node.distance:
            link.to_node.distance = distance
            heapq.heappush(q, QueueObject(link.to_node))

print(nodes[N - 1].distance)
