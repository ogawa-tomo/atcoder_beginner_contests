N, M, K = map(int, input().split())

# answer_num[i]: 人iの正解数
answer_num: list[int] = [0] * N
perfect_people: list[int] = []
for _ in range(K):
    a, b = map(int, input().split())
    a -= 1
    answer_num[a] += 1
    if answer_num[a] == M:
        perfect_people.append(a + 1)

print(" ".join([str(p) for p in perfect_people]))
