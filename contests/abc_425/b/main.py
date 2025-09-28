N = int(input())
A = list(map(int, input().split()))

# emerge[i]: iが登場した回数
emerge = [0] * (N + 1)
# print(emerge)
for a in A:
    if a == -1:
        continue
    if emerge[a] == 1:
        print("No")
        exit()
    emerge[a] = 1

usable: list[int] = []
for i in range(1, N + 1):
    if emerge[i] == 0:
        usable.append(i)

# print(usable)


answer: list[int] = []
for a in A:
    if a == -1:
        answer.append(usable.pop())
        # print(usable)
    else:
        answer.append(a)
print("Yes")
print(" ".join([str(ans) for ans in answer]))
