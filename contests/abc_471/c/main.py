import sys


N = int(input())
A = list(map(int, input().split()))

A.append(0)
A.sort()
# print(A)

index = 0
for i in range(N):
    a = A[i]
    if a == 0:
        index = i
        break

distance = 0
eaten_cookies = 0
# 左右それぞれいくつ先のクッキーを拾えばいいか
left_diff = 1
right_diff = 1
while eaten_cookies < N:
    left = index - left_diff
    right = index + right_diff
    # print(index, left, right)

    if 0 <= left and right < N + 1:
        left_distance = A[index] - A[left]
        right_distance = A[right] - A[index]
        if left_distance <= right_distance:
            distance += left_distance
            index = left
            right_diff += left_diff
            left_diff = 1
        else:
            distance += right_distance
            index = right
            left_diff += right_diff
            right_diff = 1

    elif left < 0:
        # 左にはいけない
        right_distance = A[right] - A[index]
        left_diff = sys.maxsize
        distance += right_distance
        index = right
        right_diff = 1
    else:
        left_distance = A[index] - A[left]
        right_diff = sys.maxsize
        distance += left_distance
        index = left
        left_diff = 1

    # elif 0 <= left:
    #     left_distance = A[index] - A[left]
    #     right_distance = sys.maxsize
    # else:
    #     left_distance = sys.maxsize
    #     right_distance = A[right] - A[index]

    eaten_cookies += 1

print(distance)
