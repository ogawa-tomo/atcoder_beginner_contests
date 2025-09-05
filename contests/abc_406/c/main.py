N = int(input())
P = list(map(int, input().split()))


class Top:
    def __init__(self, up_count: int):
        self.up_count = up_count


current_top: Top | None = None
# 'beggining', 'up', 'down'
status = "beginning"
up_count = 0
down_count = 0
answer = 0
for i in range(N):
    current = P[i]
    if i == 0:
        continue
    before = P[i - 1]

    # 上がる
    if current > before:
        if status != "down":
            # 上り坂
            up_count += 1
        else:
            # 谷

            up_count = 1
        status = "up"
    # 下がる
    else:
        if status != "up":
            # 下り坂
            down_count += 1
        else:
            # 山
            if current_top is not None:
                answer += current_top.up_count * up_count
            current_top = Top(up_count)
            down_count = 1
        status = "down"

if status == "up" and current_top is not None:
    answer += current_top.up_count * up_count

print(answer)
