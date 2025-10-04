S = list(input())

emerged: list[str] = []
two = ""
for s in S:
    if s in emerged:
        two = s
    emerged.append(s)

for s in S:
    if s != two:
        print(s)
        exit()
