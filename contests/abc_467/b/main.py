N = int(input())

answer = 0
for _ in range(N):
    q = input().split()
    # print(q)
    a = int(q[0])
    b = int(q[1])
    s = q[2]

    if s == "keep":
        answer += b - a

print(answer)
