from collections import deque


N = int(input())


class Node:
    def __init__(self) -> None:
        self.links: list[Link] = []
        self.reverse_links: list[Link] = []
        self.distance = -1


class Link:
    def __init__(self, to_node: Node, label: str):
        self.to_node = to_node
        self.label = label


nodes = [Node() for _ in range(N)]

for i in range(N):
    links = list(input())
    for j in range(N):
        label = links[j]
        if label == "-":
            continue
        from_node = nodes[i]
        to_node = nodes[j]
        from_node.links.append(Link(to_node, label))
        to_node.reverse_links.append(Link(from_node, label))


def reset_distance():
    for node in nodes:
        node.distance = -1


for i in range(N):
    for j in range(N):
        from_node = nodes[i]
        to_node = nodes[j]
        d: deque[Node] = deque()
        d.append(from_node)
        from_node.distance = 0
        while d:
            node = d.popleft()
            distance = node.distance
            for link in node.links:
                neighbor = link.to_node
                if neighbor.distance == -1:
                    d.append(neighbor)
