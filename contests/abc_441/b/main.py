N, M = map(int, input().split())
S = set(input())
T = set(input())
Q = int(input())
# print(S)
for _ in range(Q):
    w = input()
    takahashi = True
    aoki = True
    for c in w:
        if c not in S:
            takahashi = False
            break
        if c not in T:
            aoki = False
            break
    if takahashi and aoki:
        print("Unknown")
    elif takahashi:
        print("Takahashi")
    else:
        print("Aoki")
