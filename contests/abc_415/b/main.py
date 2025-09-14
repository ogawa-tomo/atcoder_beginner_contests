S = list(input())
# print(S)

N = len(S)
while True:
    indice: list[int] = []
    for i in range(N):
        s = S[i]
        if s == "#":
            indice.append(i)
            S[i] = "."
            if len(indice) == 2:
                break
    if len(indice) == 2:
        print(",".join([str(i + 1) for i in indice]))
    else:
        break
