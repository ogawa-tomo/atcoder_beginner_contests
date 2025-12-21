H, W, N = map(int, input().split())
grids: list[list[int]] = []
for _ in range(H):
    row = list(map(int, input().split()))
    grids.append(row)

# print(grids)
nums: list[int] = []
for _ in range(N):
    b = int(input())
    nums.append(b)

answer = 0
for i in range(H):
    # i行目
    tmp_answer = 0
    row = grids[i]
    for b in nums:
        c = row.count(b)
        tmp_answer += c
    # print(tmp_answer)
    answer = max(answer, tmp_answer)
print(answer)
