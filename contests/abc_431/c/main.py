N, M, K = map(int, input().split())
H = list(map(int, input().split()))
B = list(map(int, input().split()))

H.sort(reverse=True)
B.sort(reverse=True)
# print(H)
# print(B)
h_index = 0
b_index = 0
num = 0
while h_index < N and b_index < M:
    head = H[h_index]
    body = B[b_index]
    if body >= head:
        num += 1
        if num == K:
            print("Yes")
            exit()
        h_index += 1
        b_index += 1
    else:
        h_index += 1

print("No")
