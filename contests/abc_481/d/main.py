import heapq
import sys

max_distance = sys.maxsize


class Node:
    def __init__(self, i: int) -> None:
        self.i = i
        self.distance = max_distance
        self.to_nodes: list[Node] = []
        self.finalized = False

    def __repr__(self):
        return str(self.distance)


# キューには同じノードが追加されることがある。
# キューに追加済みのノードに対してdistanceを操作すると、キューが正常に動作しない。
# したがって、キューに追加するための専用のクラスを用意する。
class QueueObject:
    def __init__(self, node: Node):
        self.node = node
        self.distance = node.distance

    def __lt__(self, other):
        return self.distance < other.distance

    def __repr__(self):
        return str(self.distance)


def dijkstra(start_node: Node):
    q: list[QueueObject] = []
    start_node.distance = 0

    heapq.heappush(q, QueueObject(start_node))
    while q:
        queue_object = heapq.heappop(q)
        node = queue_object.node

        if node.finalized:
            continue
        node.finalized = True

        for i in range(len(node.to_nodes)):
            to_node = node.to_nodes[i]
            distance = node.distance
            if i > 0:
                distance += 1
            if distance < to_node.distance:
                to_node.distance = distance
                heapq.heappush(q, QueueObject(to_node))


N, M, S, T = map(int, input().split())

nodes = [Node(i) for i in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    node_a = nodes[a]
    node_b = nodes[b]
    node_a.to_nodes.append(node_b)

for node in nodes:
    node.to_nodes.sort(key=lambda n: n.i)
    # print(node, node.to_nodes)

start_node = nodes[S - 1]
goal_node = nodes[T - 1]

dijkstra(start_node)

if goal_node.distance == max_distance:
    print(-1)
else:
    print(goal_node.distance)
