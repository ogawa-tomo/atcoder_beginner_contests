S = list(input())
# print(S)

num = 0
index = 0
while index < len(S):
    if S[index] == "0" and index < len(S) - 1 and S[index + 1] == "0":
        num += 1
        index += 2
    else:
        num += 1
        index += 1
print(num)
