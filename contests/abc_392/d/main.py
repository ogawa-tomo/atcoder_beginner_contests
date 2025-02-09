import itertools

N = int(input())


class Dice:
    def __init__(self, surface_num: int, surfaces: list[int]):
        self.surface_num = surface_num
        self.surfaces = surfaces
        # value_num[value]: 値がvalueである面の数
        self.value_num = [0] * (10**5 + 1)
        # self.value_num = [0] * (10)
        # 重複なしの値
        self.distinct_values = set()
        for value in self.surfaces:
            self.value_num[value] += 1
            self.distinct_values.add(value)

    # valueが出る確率
    def probability(self, value):
        return self.value_num[value] / self.surface_num

    def __repr__(self):
        return f"[{self.surface_num}, {self.surfaces}]"


dices: list[Dice] = []
for _ in range(N):
    input_list = list(map(int, input().split()))
    K = input_list[0]
    A = input_list[1:]
    # print(K)
    # print(A)
    dice = Dice(K, A)
    dices.append(dice)

# for dice in dices:
#     print(dice)
#     print(dice.value_num)

answer = 0
for combination in itertools.combinations(dices, 2):
    # print(combination)
    dice1 = combination[0]
    dice2 = combination[1]
    # print(dice1, dice2)
    p = 0
    for value in dice1.distinct_values:
        p += dice1.probability(value) * dice2.probability(value)
    answer = max(p, answer)
print(answer)
