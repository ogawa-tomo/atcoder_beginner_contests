import sys

N, Q = map(int, input().split())
X = list(map(int, input().split()))

answer: list[int] = []

# boxes[i]: 箱iに入っているボールの数
boxes: list[int] = [0] * N


def min_box_index():
    min_num = sys.maxsize
    for i in range(N):
        num = boxes[i]
        if num < min_num:
            result = i
            min_num = num
    return result


min_box = 1
for x in X:
    if x > 0:
        answer.append(x)
        boxes[x - 1] += 1
        continue
    index = min_box_index()
    answer.append(index + 1)
    boxes[index] += 1

print(" ".join([str(a) for a in answer]))
