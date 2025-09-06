N, L = map(int, input().split())
D = list(map(int, input().split()))

# num[i]: i進んだ位置にある点の数
num: list[int] = [0] * L

if L % 3 != 0:
    print(0)
    exit()

num[0] = 1
l = 0
for d in D:
    l += d
    l %= L
    num[l] += 1


# print(num)

answer = 0
length = L // 3
for i in range(length):
    if num[i] > 0 and num[i + length] > 0 and num[i + 2 * length] > 0:
        answer += num[i] * num[i + length] * num[i + 2 * length]

print(answer)
