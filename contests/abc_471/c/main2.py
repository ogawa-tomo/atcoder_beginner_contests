import sys


N = int(input())
A = list(map(int, input().split()))

plus_list: list[int] = []
minus_list: list[int] = []
for a in A:
    if a > 0:
        plus_list.append(a)
    else:
        minus_list.append(a)

plus_list.sort(reverse=True)
minus_list.sort()

point = 0
answer = 0
while plus_list or minus_list:
    if plus_list:
        plus_distance = plus_list[-1] - point
    else:
        plus_distance = sys.maxsize

    if minus_list:
        minus_distance = point - minus_list[-1]
    else:
        minus_distance = sys.maxsize

    if minus_distance <= plus_distance:
        answer += minus_distance
        point = minus_list.pop()
    else:
        answer += plus_distance
        point = plus_list.pop()

print(answer)
