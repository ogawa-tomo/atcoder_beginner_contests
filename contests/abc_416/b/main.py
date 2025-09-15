S = list(input())

T: list[str] = []

in_sharp = True
for s in S:
    if s == "#":
        T.append("#")
        in_sharp = True
        continue
    if in_sharp:
        T.append("o")
        in_sharp = False
    else:
        T.append(".")

print("".join(T))
