# TLE
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


class DFS:
    def __init__(self, goal_node: Node) -> None:
        self.costs: set[int] = set()
        self.goal_node = goal_node
        self.ok = False

    def dfs(self, node: Node, current_cost: int, num: int):
        if num == L:
            if S <= current_cost <= T and node == self.goal_node:
                self.costs.add(current_cost)
                self.ok = True
            return
        for link in node.links:
            cost = link.cost
            to_node = link.to_node
            self.dfs(to_node, current_cost + cost, num + 1)


d = DFS(nodes[0])
d.dfs(nodes[0], 0, 0)
# print(d.costs)
# print(d.ok)
# print(hoge)

ok_nodes: list[Node] = []
for node in nodes:
    d = DFS(node)
    d.dfs(nodes[0], 0, 0)
    # print(d.ok)
    if d.ok:
        ok_nodes.append(node)

print(" ".join([str(node.i + 1) for node in ok_nodes]))
