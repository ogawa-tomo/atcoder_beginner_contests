# ほかの解法でも解けそう
N, M = map(int, input().split())


class Node:
    def __init__(self) -> None:
        self.neighbors: list[Node] = []
        # self.visited = False
        self.visited_count = 0


nodes = [Node() for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    node_a = nodes[a]
    node_b = nodes[b]
    node_a.neighbors.append(node_b)
    node_b.neighbors.append(node_a)

start_node = nodes[0]
current_node = nodes[0]
node_count = 0
while True:
    node_count += 1
    # current_node.visited = True
    current_node.visited_count = node_count
    if len(current_node.neighbors) != 2:
        # print("hoge")
        print("No")
        exit()
    next_node = current_node.neighbors[0]
    if next_node.visited_count == node_count - 1:
        next_node = current_node.neighbors[1]

    if node_count == N:
        if next_node == start_node:
            print("Yes")
            exit()
        else:
            # print("fuga")
            print("No")
            exit()
    if next_node.visited_count > 0:
        # print("piyo")
        print("No")
        exit()
    current_node = next_node
