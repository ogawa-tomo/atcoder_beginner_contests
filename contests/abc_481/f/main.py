# WA
import heapq
import sys

max_distance = sys.maxsize


class Node:
    def __init__(self) -> None:
        self.distance = max_distance
        self.digits_num = max_distance
        self.links: list[Link] = []
        self.finalized = False
        self.route: list[Node] = []

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
        self.digits_num = node.digits_num

    def __lt__(self, other):
        return self.distance < other.distance
        # if self.digits_num == other.digits_num:
        #     return self.distance < other.distance
        # return self.digits_num < other.digits_num

    def __repr__(self):
        return str(self.distance)


def dijkstra(start_node: Node):
    q: list[QueueObject] = []
    start_node.distance = 0
    start_node.digits_num = 0

    heapq.heappush(q, QueueObject(start_node))
    while q:
        queue_object = heapq.heappop(q)
        node = queue_object.node

        if node.finalized:
            continue
        node.finalized = True

        for link in node.links:
            to_node = link.to_node
            # 10**5桁の文字列を数値に変換できないのでダメ
            distance = int(str(node.distance) + str(link.distance))
            # これでもだめ
            # distance = node.distance * 10 + link.distance
            digits_num = node.digits_num + 1
            # if digits_num < to_node.digits_num:
            if distance < to_node.distance:
                to_node.distance = distance
                to_node.digits_num = digits_num
                heapq.heappush(q, QueueObject(to_node))
            # elif digits_num == to_node.digits_num:
            #     if distance < to_node.distance:
            #         to_node.distance = distance
            #         heapq.heappush(q, QueueObject(to_node))


N, M = map(int, input().split())
MOD = 998244353

nodes = [Node() for _ in range(N)]
for _ in range(M):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    node_a = nodes[a]
    node_b = nodes[b]
    link = Link(c, node_b)
    node_a.links.append(link)

dijkstra(nodes[0])

for i in range(1, N):
    node = nodes[i]
    print(node.distance % MOD)
    # print(node.distance)


# これがエラーになる
# print(int("1" * 10**5))
