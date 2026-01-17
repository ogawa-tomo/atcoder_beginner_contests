# AC
class Node:
    def __init__(self, i: int) -> None:
        self.i = i
        self.links: list[Link] = []

    def __repr__(self):
        return str(self.i)

    def __lt__(self, other):
        return self.i < other.i


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


class DFS:
    def __init__(self) -> None:
        self.ok_nodes: set[Node] = set()

    def dfs(self, node: Node, current_cost: int, num: int):
        # print(node, current_cost, num)
        if num == L:
            # print("L")
            # print(node, current_cost)
            if S <= current_cost <= T:
                self.ok_nodes.add(node)
            return
        for link in node.links:
            cost = link.cost
            to_node = link.to_node
            self.dfs(to_node, current_cost + cost, num + 1)


d = DFS()
d.dfs(nodes[0], 0, 0)
# print(d.ok_nodes)

answer_nodes = list(d.ok_nodes)
answer_nodes.sort()
print(" ".join([str(node.i + 1) for node in answer_nodes]))
