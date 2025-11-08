X = int(input())
N = int(input())
W = list(map(int, input().split()))
Q = int(input())

weight = X
# equipments[i]: 部品iがついているかどうか
equipments = [False] * N
for _ in range(Q):
    p = int(input())
    p -= 1
    part_weight = W[p]
    if equipments[p]:
        equipments[p] = False
        weight -= part_weight
    else:
        equipments[p] = True
        weight += part_weight
    print(weight)
