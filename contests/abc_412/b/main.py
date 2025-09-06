S = list(input())
T = list(input())

for i in range(1, len(S)):
    s = S[i]
    # print(s)
    if s.isupper():
        prev = S[i - 1]
        if prev not in T:
            print("No")
            exit()

print("Yes")
