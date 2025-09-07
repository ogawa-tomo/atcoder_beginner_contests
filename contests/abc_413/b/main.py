N = int(input())
letters: set[str] = set()

S: list[str] = []
for _ in range(N):
    s = input()
    S.append(s)

# print(S)
for i in range(N):
    for j in range(N):
        if i == j:
            continue
        si = S[i]
        sj = S[j]
        letter = si + sj
        letters.add(letter)

# print(letters)
print(len(letters))
