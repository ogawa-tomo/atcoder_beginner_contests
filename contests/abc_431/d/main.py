# WA
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

head_parts.sort()
# print(head_parts, head_weight)
# print(body_parts, body_weight)

# 重心とれるまでひとつずつbodyに移す
for head_part in head_parts:
    if body_weight >= head_weight:
        break
    head_weight -= head_part.weight
    head_point -= head_part.head_point
    body_weight += head_part.weight
    body_point += head_part.body_point

print(body_point + head_point)
