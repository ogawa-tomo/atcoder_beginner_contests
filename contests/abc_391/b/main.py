N, M = map(int, input().split())

S: list[list[str]] = []
for _ in range(N):
    row = list(input())
    S.append(row)
T: list[list[str]] = []
for _ in range(M):
    row = list(input())
    T.append(row)
# print(S)
# print(T)


def is_same(Si: int, Sj: int):
    for i in range(M):
        for j in range(M):
            if S[Si + i][Sj + j] != T[i][j]:
                return False
    return True


answer = 0
for Si in range(N - M + 1):
    for Sj in range(N - M + 1):
        if is_same(Si, Sj):
            print(Si + 1, Sj + 1)
