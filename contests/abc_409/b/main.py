N = int(input())
A = list(map(int, input().split()))

answer = 0

# 数列内にある数字のみを候補としているのが誤り
# A.sort()
# # print(A)
# for i in range(N):
#     if N - i >= A[i]:
#         answer = A[i]
#         # print(i, answer)
# print(answer)

# 数列内にある数字のみを候補としているのが誤り
# for a in A:
#     times = 0
#     for b in A:
#         if b >= a:
#             times += 1
#     print(a, times)
#     if times >= a:
#         answer = max(answer, a)
# print(answer)

for x in range(N + 1):
    count = 0
    for a in A:
        if a >= x:
            count += 1
    if count >= x:
        answer = x
print(answer)
