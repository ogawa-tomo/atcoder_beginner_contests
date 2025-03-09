# 全順序を列挙する解法
import sys
import itertools


N, M = map(int, input().split())


class Node:
    def __init__(self, index: int) -> None:
        self.links: list[Link] = []
        self.visited = False
        self.index = index

    def to_nodes(self):
        nodes = []
        for link in self.links:
            nodes.append(link.to_node)
        return nodes

    def label_to_node(self, to_node):
        for link in self.links:
            if link.to_node.index == to_node.index:
                return link.label
        return 0

    def __repr__(self):
        return str(self.index)


class Link:
    def __init__(self, label: int, to_node: Node):
        self.label = label
        self.to_node = to_node


nodes = [Node(i) for i in range(N)]


for _ in range(M):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    node_u = nodes[u]
    node_v = nodes[v]
    node_u.links.append(Link(w, node_v))
    node_v.links.append(Link(w, node_u))

all_paths = list(itertools.permutations(nodes))
# print(all_paths)


def is_linked_to_last_node(path: tuple[Node, ...]):
    for i in range(N - 1):
        if path[i].index == N - 1:
            return True
        if path[i + 1] not in path[i].to_nodes():
            return False
    return True


def score(path: tuple[Node, ...]):
    result = 0
    for i in range(N - 1):
        node = path[i]
        to_node = path[i + 1]
        # print(node)
        # print(to_node)
        result ^= node.label_to_node(to_node)
        # print(result)
        if to_node.index == N - 1:
            return result
    return result


answer = sys.maxsize
for path in all_paths:
    if path[0].index != 0:
        continue
    if not is_linked_to_last_node(path):
        continue
    # print(path)
    answer = min(score(path), answer)
print(answer)
