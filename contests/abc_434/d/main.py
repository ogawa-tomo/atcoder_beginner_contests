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


class Cloud:
    def __init__(self, min_i: int, min_j: int, max_i: int, max_j: int):
        self.min_i = min_i
        self.min_j = min_j
        self.max_i = max_i
        self.max_j = max_j


grid_length = 2000

sky: list[list[int]] = []
for _ in range(grid_length + 1):
    sky.append([0] * (grid_length + 1))

clouds: list[Cloud] = []
for _ in range(N):
    u, d, l, r = map(int, input().split())
    u -= 1
    d -= 1
    l -= 1
    r -= 1
    cloud = Cloud(u, l, d, r)
    clouds.append(cloud)

    sky[u][l] += 1
    sky[u][r + 1] -= 1
    sky[d + 1][l] -= 1
    sky[d + 1][r + 1] += 1

sky_Z: list[list[int]] = []
for _ in range(grid_length):
    sky_Z.append([0] * grid_length)
for i in range(grid_length):
    for j in range(grid_length):
        if j == 0:
            sky_Z[i][0] = sky[i][0]
            continue
        sky_Z[i][j] = sky_Z[i][j - 1] + sky[i][j]
for j in range(grid_length):
    for i in range(grid_length):
        if i == 0:
            continue
        sky_Z[i][j] = sky_Z[i - 1][j] + sky_Z[i][j]

# sky_Z[i][j]: i,jに重なっている雲の数

# for sky_z in sky_Z:
#     print(sky_z)

# only_coverd[i][j]: i, jが唯一カバーされていたら1
only_coverd: list[list[int]] = []
total_covered = 0  # 覆われているマスの数
for _ in range(grid_length):
    only_coverd.append([0] * grid_length)
for i in range(grid_length):
    for j in range(grid_length):
        covered = sky_Z[i][j]
        if covered == 1:
            only_coverd[i][j] = 1
        else:
            only_coverd[i][j] = 0
        if covered > 0:
            total_covered += 1

only_coverd_cul_sum = CumulativeSum2D(only_coverd)
# only_coverd_cul_sum.range_sum(min_i, min_j, max_i, max_j): 唯一カバーされる数
# print(total_covered)
for cloud in clouds:
    only_coverd_num = only_coverd_cul_sum.range_sum(
        cloud.min_i, cloud.min_j, cloud.max_i, cloud.max_j
    )
    # print(only_coverd_num)
    print(grid_length**2 - total_covered + only_coverd_num)
