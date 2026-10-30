# TLE
import sys

sys.setrecursionlimit(10**9)  # 10^9が限界らしく、10^10にするとREになっちゃった


class Node:
    def __init__(self, i: int) -> None:
        self.i = i
        self.to_nodes: list[Node] = []
        self.visited = False
        self.finished = False

    def __repr__(self) -> str:
        return str(self.i + 1)


class CycleDetection:
    def __init__(self, nodes: list[Node]) -> None:
        self.nodes = nodes
        self.history: list[Node] = []
        self.start_node: Node | None = None

    def dfs(self, node: Node) -> Node | None:
        node.visited = True
        self.history.append(node)
        for to_node in node.to_nodes:
            if to_node.finished:
                continue
            if to_node.visited:
                # サイクル検出

                # 偶サイクルがたくさんあるとここでたくさん空振るので、時間を使ったか…？
                # 長さを確認
                length = 0
                self.history.reverse()
                for h in self.history:
                    length += 1
                    if h == to_node:
                        break

                self.history.reverse()

                if length % 2 == 1:
                    self.start_node = to_node
                    return to_node
                else:
                    continue

            start_node = self.dfs(to_node)
            if start_node is not None:
                return start_node

        node.finished = True
        self.history.pop()

    @property
    def has_cycle(self):
        return self.start_node is not None

    def get_cycle(self):
        if not self.has_cycle:
            return None
        cycle: list[Node] = []
        while self.history:
            node = self.history.pop()
            cycle.append(node)
            if node == self.start_node:
                break
        return cycle


def get_cycle(nodes: list[Node]):
    cd = CycleDetection(nodes)
    cd.dfs(nodes[0])
    return cd.get_cycle()


T = int(input())

for _ in range(T):
    N, M = map(int, input().split())

    nodes = [Node(i) for i in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        node_a = nodes[a]
        node_b = nodes[b]
        node_a.to_nodes.append(node_b)
        node_b.to_nodes.append(node_a)

    cycle = get_cycle(nodes)
    if cycle is not None:
        print(len(cycle))
        print(*cycle)
    else:
        print(-1)
