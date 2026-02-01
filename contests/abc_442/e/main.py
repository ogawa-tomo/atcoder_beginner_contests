# 考え方は正しいのだが、浮動小数点数の誤差でWA
import math
from fractions import Fraction
from collections import defaultdict


class CumulativeSum:
    def __init__(self, _list: list[int]):
        self._list = _list
        total = 0
        self.cumulative_sum_list: list[int] = []
        for elem in self._list:
            total += elem
            self.cumulative_sum_list.append(total)

    def sum(self, index: int):
        if index == -1:
            return 0
        return self.cumulative_sum_list[index]

    def range_sum(self, left_index: int, right_index: int):
        return self.sum(right_index) - self.sum(left_index - 1)


class Monster:
    def __init__(self, i: int, theta: int | float):
        self.i = i
        self.theta = theta

    def __repr__(self):
        return str(self.theta)


N, Q = map(int, input().split())

monsters: list[Monster] = []
theta_set: set[int | float] = set()
# monsters_by_theta[t]: 角度tにいるモンスターのリスト
monsters_by_theta: defaultdict[int | float, list[Monster]] = defaultdict(list)
for i in range(N):
    x, y = map(int, input().split())
    theta: int | float = 0
    if x == 0:
        if y > 0:
            theta = 90
        else:
            theta = 270
    else:
        theta = math.degrees(math.atan2(y, x))
        if y < 0:
            theta += 360
    print(theta)
    monster = Monster(i, theta)
    monsters.append(monster)
    monsters_by_theta[theta].append(monster)
    theta_set.add(theta)

thetas = list(theta_set)
thetas.sort(reverse=True)
# print(thetas)
# print(monsters)
# print(monsters_by_theta)


# theta_index[t]: 角度tが何番目に小さい角度か
theta_index: defaultdict[int | float, int] = defaultdict(int)
for i, theta in enumerate(thetas):
    theta_index[theta] = i
# print(theta_index)

# num_monsters[i]: i番目に小さい角度にいるモンスターの数
num_monsters: list[int] = []
for i, theta in enumerate(thetas):
    monsters_in_theta = monsters_by_theta[theta]
    # print(theta, monsters_in_theta)
    num_monsters.append(len(monsters_in_theta))

# print(num_monsters)
# print(theta_index)

cum_sum = CumulativeSum(num_monsters)
# print(cum_sum.range_sum(2, 3))

theta_num = len(thetas)

for _ in range(Q):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    monster_a = monsters[a]
    monster_b = monsters[b]
    # aの角度が何番目に小さい角度か
    a_index = theta_index[monster_a.theta]
    b_index = theta_index[monster_b.theta]

    # print(monster_a.theta, monster_b.theta)
    # print(a_index, b_index)

    if a_index <= b_index:
        print(cum_sum.range_sum(a_index, b_index))
    else:
        # print("hoge")
        # print(b_index, theta_num - 1)
        # print(cum_sum.range_sum(a_index, theta_num - 1))
        # print(cum_sum.range_sum(0, a_index))
        answer = cum_sum.range_sum(a_index, theta_num - 1) + cum_sum.range_sum(
            0, b_index
        )
        print(answer)
