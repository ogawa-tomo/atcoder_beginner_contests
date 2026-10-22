N, K = map(int, input().split())
A = list(map(int, input().split()))

sorted_A = sorted(A)
# print(A)
# print(sorted_A)

# 両端から数えて一致がN-K個あればよい
matched = 0
for i in range(N):
    if A[i] == sorted_A[i]:
        matched += 1
    else:
        break

for i in range(N - 1, -1, -1):
    # print(A[i], sorted_A[i])
    if A[i] == sorted_A[i]:
        matched += 1
    else:
        break

if matched >= N - K:
    print("Yes")
else:
    print("No")
