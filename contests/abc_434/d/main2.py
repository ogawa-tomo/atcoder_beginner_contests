class Cover:
    def __init__(self, min_i: int, min_j: int, max_i: int, max_j: int):
        self.min_i = min_i
        self.min_j = min_j
        self.max_i = max_i
        self.max_j = max_j


class Covered2D:
    def __init__(self, covers: list[Cover], H: int, W: int):

        # (i, j)における差分
        x: list[list[int]] = []
        for _ in range(H + 1):
            x.append([0] * (W + 1))
        for cover in covers:
            x[cover.min_i][cover.min_j] += 1
            x[cover.min_i][cover.max_j + 1] -= 1
            x[cover.max_i + 1][cover.min_j] -= 1
            x[cover.max_i + 1][cover.max_j + 1] += 1

        # 累積和を求める
        self.grids: list[list[int]] = []
        for _ in range(H):
            self.grids.append([0] * W)
        for i in range(H):
            for j in range(W):
                if j == 0:
                    self.grids[i][j] = x[i][j]
                    continue
                self.grids[i][j] = self.grids[i][j - 1] + x[i][j]
        for j in range(W):
            for i in range(H):
                if i == 0:
                    continue
                self.grids[i][j] = self.grids[i - 1][j] + self.grids[i][j]


class CumulativeSum2D:
    def __init__(self, grids: list[list[int]]):
        self.grids = grids
        self.cum_sum_grids: list[list[int]] = []
        for i in range(len(grids)):
            row_cum_sum: list[int] = []
            total = 0
            for j in range(len(grids[i])):
                total += grids[i][j]
                row_cum_sum.append(total)
            self.cum_sum_grids.append(row_cum_sum)
        for i in range(len(grids)):
            if i == 0:
                continue
            for j in range(len(grids[i])):
                self.cum_sum_grids[i][j] += self.cum_sum_grids[i - 1][j]

    def range_sum(self, min_i, min_j, max_i, max_j):
        if min_i == 0 and min_j == 0:
            return self.cum_sum_grids[max_i][max_j]
        elif min_i == 0 and min_j > 0:
            return (
                self.cum_sum_grids[max_i][max_j] - self.cum_sum_grids[max_i][min_j - 1]
            )
        elif min_i > 0 and min_j == 0:
            return (
                self.cum_sum_grids[max_i][max_j] - self.cum_sum_grids[min_i - 1][max_j]
            )
        else:
            return (
                self.cum_sum_grids[max_i][max_j]
                - self.cum_sum_grids[max_i][min_j - 1]
                - self.cum_sum_grids[min_i - 1][max_j]
                + self.cum_sum_grids[min_i - 1][min_j - 1]
            )


N = int(input())


grid_length = 2000

clouds: list[Cover] = []
for _ in range(N):
    u, d, l, r = map(int, input().split())
    u -= 1
    d -= 1
    l -= 1
    r -= 1
    cloud = Cover(u, l, d, r)
    clouds.append(cloud)

# sky[i][j]: i,jに重なっている雲の数
sky = Covered2D(clouds, grid_length, grid_length).grids

# only_coverd[i][j]: i, jが唯一カバーされていたら1
only_coverd: list[list[int]] = []
total_covered = 0  # 覆われているマスの数
for _ in range(grid_length):
    only_coverd.append([0] * grid_length)
for i in range(grid_length):
    for j in range(grid_length):
        covered = sky[i][j]
        if covered == 1:
            only_coverd[i][j] = 1
        else:
            only_coverd[i][j] = 0
        if covered > 0:
            total_covered += 1

only_coverd_cul_sum = CumulativeSum2D(only_coverd)
# only_coverd_cul_sum.range_sum(min_i, min_j, max_i, max_j): 唯一カバーされる数
for cloud in clouds:
    only_coverd_num = only_coverd_cul_sum.range_sum(
        cloud.min_i, cloud.min_j, cloud.max_i, cloud.max_j
    )
    print(grid_length**2 - total_covered + only_coverd_num)
