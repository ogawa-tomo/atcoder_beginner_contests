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


N, M, C = map(int, input().split())
A = list(map(int, input().split()))

# num_dict[p]: 地点pにいる人数
num_dict: defaultdict[int, int] = defaultdict(int)
point_set: set[int] = set()  # 人がいる地点の集合
for a in A:
    point_set.add(a)
    num_dict[a] += 1
# print(num_dict)

# points: 人がいる地点のリスト
points = sorted(list(point_set))

# nums[i]: 人がいる地点のi番目にいる人の数
nums: list[int] = []
for p in points:
    nums.append(num_dict[p])

added_points: list[int] = []
for point in points:
    added_points.append(M + point)
points.extend(added_points)
# # print("points", points)
nums.extend(nums)
# # print("nums", nums)

cs = CumulativeSum(nums)

answer = 0
# left, right: 人がいる地点のリストのleft番目、right番目
right = 1
length = len(points) // 2
for left in range(length):
    if left == right:
        right += 1
    while cs.range_sum(left + 1, right) < C:
        right += 1
    left_point = points[left]
    next_left_point = points[left + 1]
    answer += cs.range_sum(left + 1, right) * (next_left_point - left_point)
print(answer)
