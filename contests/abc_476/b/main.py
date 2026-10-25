N = int(input())
S = input()
T = input()

for i in range(N):
    s = S[i]
    t = T[i]
    if t != "*" and s != t:
        print("No")
        exit()

print("Yes")
