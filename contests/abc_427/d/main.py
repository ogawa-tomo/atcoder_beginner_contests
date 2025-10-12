class Node:
    def __init__(self, i: int) -> None:
        self.i = i
        self.to_nodes: set[Node] = set()
        self.s = ""

    def __repr__(self):
        return str(self.i)


# 引数で与えられたノードにしか行けないノード
def only_to_nodes(to_nodes: set[Node]):
    result: set[Node] = set()
    for node in nodes:
        if node.to_nodes <= to_nodes:
            result.add(node)
    return result


# 引数で与えられたノードのどれかに行けるノード
def can_to_nodes(to_nodes: set[Node]):
    result: set[Node] = set()
    for node in nodes:
        if node.to_nodes & to_nodes:
            result.add(node)
    return result


T = int(input())
for _ in range(T):
    N, M, K = map(int, input().split())
    nodes = [Node(i) for i in range(N)]
    A_nodes: set[Node] = set()
    S = list(input())
    for i in range(N):
        node = nodes[i]
        string = S[i]
        node.s = string
        if string == "A":
            A_nodes.add(node)
    for _ in range(M):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        node_u = nodes[u]
        node_v = nodes[v]
        node_u.to_nodes.add(node_v)

    # Aliceの勝ちパターンを探す
    to_nodes = A_nodes
    for k in range(K):
        # Bobの手番。to_nodesにしか行けないノードを探す
        to_nodes = only_to_nodes(to_nodes)
        # Aliceの手番。to_nodesに行けるノードを探す
        to_nodes = can_to_nodes(to_nodes)
    # to_nodesが存在し出発ノードが含まれていればAliceの勝ち
    if nodes[0] in to_nodes:
        print("Alice")
    else:
        print("Bob")
