N, M = map(int, input().split())
A = list(map(int, input().split()))

# print(A)
# print(A.pop())
# print(A)

# exists = False
# for a in A:
#     if a <= M:
#         exists = True
#         break
# if not exists:
#     print(0)
#     exit()

d: dict = {}
for i in range(1, M + 1):
    d[i] = 0
for a in A:
    if a > M:
        continue
    d[a] += 1

for i in range(1, M + 1):
    if d[i] == 0:
        print(0)
        exit()

count = 0
while True:
    count += 1
    v = A.pop()
    if v <= M:
        d[v] -= 1
        if d[v] == 0:
            print(count)
            exit()
