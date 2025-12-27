# ためしに書いただけ
class Node:
    def __init__(self, i: int):
        self.i = i
        self.to_node: Node | None = None
        self.seen = False
        self.finished = False
        self.in_cycle = False

    def __repr__(self):
        return str(self.i)


N, Q = map(int, input().split())
A = [0, *list(map(int, input().split()))]
nodes = [Node(i) for i in range(N + 1)]

for i in range(N + 1):
    a = A[i]
    nodes[i].to_node = nodes[a]

# print(nodes)
# for node in nodes:
#     print(node, node.to_node)

cycles: list[list[Node]] = []


def dfs(node: Node):
    if node.to_node is None:
        raise
    node.seen = True

    to_node = node.to_node

    if to_node.finished:
        return True
    if to_node.seen and not to_node.finished:
        return True
    if dfs(to_node):
        return True

    to_node.finished = True
    return False


print(dfs(nodes[1]))
# print(buckets)
for _ in range(Q):
    t, b = map(int, input().split())
