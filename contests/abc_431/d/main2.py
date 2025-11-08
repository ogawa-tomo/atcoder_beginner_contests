# TLE
import sys

sys.setrecursionlimit(10**9)  # 10^9が限界らしく、10^10にするとREになっちゃった


class Part:
    def __init__(self, weight: int, head_point: int, body_point: int):
        self.weight = weight
        self.head_point = head_point
        self.body_point = body_point
        self.head_body_point_diff = self.head_point - self.body_point

    def __lt__(self, other):
        return self.head_body_point_diff < other.head_body_point_diff

    def __repr__(self):
        return str(
            [self.weight, self.head_point, self.body_point, self.head_body_point_diff]
        )


N = int(input())
head_weight = 0
head_point = 0
body_point = 0
body_weight = 0
head_parts: list[Part] = []
body_parts: list[Part] = []
for _ in range(N):
    w, h, b = map(int, input().split())
    part = Part(w, h, b)
    if b >= h:
        body_parts.append(part)
        body_point += b
        body_weight += w
    else:
        head_parts.append(part)
        head_point += h
        head_weight += w

weight_diff = head_weight - body_weight
# print(weight_diff)
if weight_diff <= 0:
    print(head_point + body_point)
    exit()

print(head_parts, head_weight)
print(body_parts, body_weight)
# print(head_point + body_point)

# いま、理想の状態
# head_partsから、重さがweight_diffをギリ超える選び方のパターンを抽出する

head_part_num = len(head_parts)


# current_indexの手前までのパーツを選んでいる状態での、最小のポイント
def min_point(current_index: int, current_weight: int, current_point: int):
    # print(current_index, current_weight, current_point)
    if current_weight >= weight_diff:
        # print("current_point", current_point)
        return current_point
    if current_index == head_part_num:
        return sys.maxsize
    # 次の1つを選ぶ
    point = sys.maxsize
    for index in range(current_index, head_part_num):
        part = head_parts[index]
        # print("part", part)
        point = min(
            point,
            min_point(
                index + 1,
                current_weight + part.weight * 2,
                current_point + part.head_body_point_diff,
            ),
        )
    return point


point = min_point(0, 0, 0)
print(head_point + body_point - point)
