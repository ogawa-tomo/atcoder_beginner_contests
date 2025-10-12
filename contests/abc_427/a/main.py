S = list(input())
length = len(S)
mid = (length - 1) // 2

print("".join([*S[:mid], *S[mid + 1 :]]))
