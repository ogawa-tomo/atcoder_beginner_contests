import heapq
import sys

max_distance = sys.maxsize


class Node:
    def __init__(self) -> None:
        self.distance = max_distance
        self.to_links: list[Link] = []
        self.finalized = False

    def __repr__(self):
        return str(self.distance)


class Link:
    def __init__(self, distance: int, to_node: Node):
        self.distance = distance
        self.to_node = to_node


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

        for to_link in node.to_links:
            to_node = to_link.to_node
            distance = node.distance + to_link.distance
            if distance < to_node.distance:
                to_node.distance = distance
                heapq.heappush(q, QueueObject(to_node))


class CumulativeSum:
    def __init__(self, _list: list[int]):
        self._list = _list
        total = 0
        self.cumulative_sum_list: list[int] = []
        for elem in self._list:
            total += elem
            self.cumulative_sum_list.append(total)

    def sum(self, index: int):
        if index == -1:
            return 0
        return self.cumulative_sum_list[index]

    def range_sum(self, left_index: int, right_index: int):
        return self.sum(right_index) - self.sum(left_index - 1)


N, Q = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))


cum_sum = CumulativeSum(A)

nodes = [Node() for _ in range(N + 1)]
last_node = nodes[N]
for i in range(N):
    node = nodes[i]

    a = A[i]
    if i < N - 1:
        to_node = nodes[i + 1]
    else:
        to_node = nodes[0]
    node.to_links.append(Link(a, to_node))
    to_node.to_links.append(Link(a, node))

    b = B[i]
    node.to_links.append(Link(b, last_node))
    last_node.to_links.append(Link(b, node))

dijkstra(last_node)


for _ in range(Q):
    s, t = map(int, input().split())
    s -= 1
    t -= 1

    if t < N:
        forward_distance = cum_sum.range_sum(s, t - 1)
        if s > 0:
            back_distance = cum_sum.range_sum(0, s - 1) + cum_sum.range_sum(t, N - 1)
        else:
            back_distance = cum_sum.range_sum(t, N - 1)

        # ノードNを経由する距離
        distance_N = nodes[s].distance + nodes[t].distance

        distance = min(forward_distance, back_distance, distance_N)
    else:
        distance = nodes[s].distance

    print(distance)
