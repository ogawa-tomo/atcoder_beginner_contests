from collections import deque


class Node:
    def __init__(self, i) -> None:
        self.i = i
        self.to_nodes: list[Node] = []
        self.parent: Node | None = None
        self.seq = 0  # 根からBFSしたときの順番
        self.subtree_size = 1
        self.visited = False
        self.x = 0

    def __repr__(self) -> str:
        return str(self.i)


class Link:
    def __init__(self, i: int, left: Node, right: Node) -> None:
        self.i = i
        self.left = left
        self.right = right


# seqとparentの調査
def bfs(start_node: Node):
    d: deque[Node] = deque()

    d.append(start_node)
    seq = 0
    start_node.seq = seq
    start_node.visited = True
    while d:
        node = d.popleft()
        for to_node in node.to_nodes:
            if not to_node.visited:
                to_node.visited = True
                seq += 1
                to_node.seq = seq
                to_node.parent = node
                d.append(to_node)


# xの計算（子孫に伝播させる）
def bfs2(start_node: Node):
    d: deque[Node] = deque()

    d.append(start_node)
    start_node.visited = True
    while d:
        node = d.popleft()
        for to_node in node.to_nodes:
            if not to_node.visited:
                to_node.visited = True
                to_node.x += node.x
                d.append(to_node)


N = int(input())

nodes = [Node(i) for i in range(N)]
links: list[Link] = []
for i in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    node_a = nodes[a]
    node_b = nodes[b]
    node_a.to_nodes.append(node_b)
    node_b.to_nodes.append(node_a)
    link = Link(i + 1, node_a, node_b)
    links.append(link)

bfs(nodes[0])


# seqを後ろから辿ることで、部分木のサイズが分かる
nodes.sort(key=lambda n: n.seq, reverse=True)
for node in nodes:
    if node.parent is not None:
        node.parent.subtree_size += node.subtree_size

nodes.sort(key=lambda n: n.i)

# リンクごとに、部分木の頂点に足すべきxを求める（子孫への伝播はあとで）
for link in links:
    if link.left.parent == link.right:
        parent = link.right
        child = link.left
    else:
        parent = link.left
        child = link.right

    child_subtree_size = child.subtree_size
    parent_subtree_size = N - child.subtree_size

    # 子が大きければ子に足し、親が大きければ根に足して子に引くことで親側だけに足す操作を実現
    if child_subtree_size > parent_subtree_size:
        child.x += link.i
    else:
        nodes[0].x += link.i
        child.x -= link.i

for node in nodes:
    node.visited = False

bfs2(nodes[0])

print(*[node.x for node in nodes])
