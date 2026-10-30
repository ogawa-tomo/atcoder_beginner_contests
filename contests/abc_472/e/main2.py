from typing import Union
import sys

sys.setrecursionlimit(10**9)


class Node:
    def __init__(self, i: int) -> None:
        self.i = i
        self.parent: Union[None, Node] = None
        self.size = 1
        self.visited = False
        self.is_black = False
        self.st_to_nodes: list[Node] = []  # 全域木を作ったときの

    @property
    def root(self):
        if self.parent is None:
            return self
        return self.parent.root

    def __repr__(self) -> str:
        return str(self.i + 1)


def is_same(node1: Node, node2: Node):
    return node1.root == node2.root


def unite(node1: Node, node2: Node):
    root1 = node1.root
    root2 = node2.root
    if root1 == root2:
        raise
    if root1.size < root2.size:
        root1.parent = root2
        root2.size += root1.size
    else:
        root2.parent = root1
        root1.size += root2.size


class Link:
    def __init__(self, from_node: Node, to_node: Node) -> None:
        self.from_node = from_node
        self.to_node = to_node


# 全域木に対して2部グラフを作る
def dfs(node: Node, is_black: bool):
    node.visited = True
    node.is_black = is_black
    for to_node in node.st_to_nodes:
        if not to_node.visited:
            dfs(to_node, not is_black)


T = int(input())

for _ in range(T):
    N, M = map(int, input().split())

    nodes = [Node(i) for i in range(N)]
    links: list[Link] = []
    for _ in range(M):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        node_a = nodes[a]
        node_b = nodes[b]
        link = Link(node_a, node_b)
        links.append(link)

    # 全域木に含まれないリンク
    except_mst_links: list[Link] = []
    for link in links:
        from_node = link.from_node
        to_node = link.to_node
        if not is_same(from_node, to_node):
            unite(from_node, to_node)
            from_node.st_to_nodes.append(to_node)
            to_node.st_to_nodes.append(from_node)
        else:
            except_mst_links.append(link)

    dfs(nodes[0], False)

    for node in nodes:
        node.visited = False

    ok = False
    for link in except_mst_links:
        from_node = link.from_node
        to_node = link.to_node

        if from_node.is_black != to_node.is_black:
            continue

        # 全域木に含まれないリンクの両端ノードの色が同じ<=>2部グラフではない<=>奇閉路が存在する
        ok = True

        path: list[Node] = []
        goal = to_node

        # pathを求める
        def dfs2(node: Node):
            if node == goal:
                path.append(node)
                return True
            node.visited = True
            for to_node in node.st_to_nodes:
                if not to_node.visited:
                    if dfs2(to_node):
                        path.append(node)
                        return True
            return False

        dfs2(from_node)
        # pathは絶対に存在する
        print(len(path))
        print(*path)
        break

    if not ok:
        print(-1)
