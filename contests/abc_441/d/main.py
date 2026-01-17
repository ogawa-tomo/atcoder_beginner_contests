# 途中
class Node:
    def __init__(self, i: int) -> None:
        self.i = i
        self.links: list[Link] = []


class Link:
    def __init__(self, cost: int, to_node: Node):
        self.cost = cost
        self.to_node = to_node


N, M, L, S, T = map(int, input().split())
nodes = [Node(i) for i in range(N)]
for _ in range(M):
    u, v, c = map(int, input().split())
    u -= 1
    v -= 1
    from_node = nodes[u]
    to_node = nodes[v]
    from_node.links.append(Link(c, to_node))


def dfs(node: Node, current_cost: int, num: int):
    if num == L:
        return current_cost
    for link in node.links:
        cost = link.cost
        to_node = link.to_node
        dfs(to_node, current_cost + cost, num + 1)


hoge = dfs(nodes[0], 0, 0)
print(hoge)
