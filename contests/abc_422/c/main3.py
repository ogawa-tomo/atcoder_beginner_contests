# 模範解答
T = int(input())
for _ in range(T):
    na, nb, nc = map(int, input().split())
    print(min(na, nc, (na + nb + nc) // 3))
