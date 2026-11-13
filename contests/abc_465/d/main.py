# TLE
import sys

sys.setrecursionlimit(10**9)  # 10^9が限界らしく、10^10にするとREになっちゃった


class DFS:
    def __init__(self, Y: int, K: int) -> None:
        self.Y = Y
        self.K = K
        self.emerged: set[tuple[int, int]] = set()

    def dfs(self, min_y: int, max_y: int, count: int) -> int | None:
        t = (min_y, max_y)
        # print(t)

        if min_y <= self.Y <= max_y:
            return count
        if t in self.emerged:
            return None
        # if min_y == max_y == 0:
        #     return None
        if min_y > 10**18:
            return None
        self.emerged.add(t)

        c1 = self.dfs(min_y // K, max_y // K, count + 1)
        c2 = self.dfs(min_y * K, max_y * K + K - 1, count + 1)

        if c1 is not None and c2 is not None:
            return min(c1, c2)
        if c1 is None and c2 is not None:
            return c2
        if c1 is not None and c2 is None:
            return c1
        return None


T = int(input())

for _ in range(T):
    X, Y, K = map(int, input().split())
    dfs = DFS(Y, K)
    answer = dfs.dfs(X, X, 0)
    # if answer is None:
    #     raise
    print(answer)
