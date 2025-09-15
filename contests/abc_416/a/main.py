N, L, R = map(int, input().split())
S = list(input())
L -= 1
R -= 1

for i in range(L, R + 1):
    if S[i] == "x":
        print("No")
        exit()
print("Yes")
