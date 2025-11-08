# AC
import sys


class Part:
    def __init__(self, weight: int, head_value: int, body_value: int):
        self.weight = weight
        self.head_value = head_value
        self.body_value = body_value
        self.head_body_value_diff = self.head_value - self.body_value

    def __lt__(self, other):
        return self.head_body_value_diff < other.head_body_value_diff

    def __repr__(self):
        return str(
            [self.weight, self.head_value, self.body_value, self.head_body_value_diff]
        )


N = int(input())
parts: list[Part] = []
value = 0
weight = 0
for _ in range(N):
    w, h, b = map(int, input().split())
    part = Part(w, h, b)
    parts.append(part)
    value += b
    weight += w

max_weight = weight // 2
# print(max_weight)

# いま、すべてがbodyにある
# bodyから、max_weightを超えない範囲で、headに移す
# そのときの、合計価値の最大値

# dp[n][w]: n個目までのpartをheadに移して、重さがwのとき、価値の最大値
dp: list[list[int]] = []
dp.append([-sys.maxsize] * (max_weight + 1))
dp[0][0] = value
# print(dp)
for n in range(1, N + 1):
    part = parts[n - 1]
    dp_row: list[int] = []
    for w in range(max_weight + 1):
        if w - part.weight >= 0:
            value = max(
                dp[n - 1][w],
                dp[n - 1][w - part.weight] - part.body_value + part.head_value,
            )
        else:
            value = dp[n - 1][w]
        dp_row.append(value)
    dp.append(dp_row)

print(max(dp[N]))
