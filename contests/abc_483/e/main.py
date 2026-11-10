# やりかけ
from itertools import combinations
import math

N, M = map(int, input().split())

if M == 2:
    print(math.comb(N, 2))
    exit()
alphabets = "abcdefghijklmnopqrstuvwxyz"
# d[i][s]: i文字目がsであるような文字のインデックスの集合
d: dict[int, dict[str, set[int]]] = dict()
for i in range(M):
    d[i] = dict()
    for s in alphabets:
        d[i][s] = set()
for index in range(N):
    S = input()
    for i in range(M):
        s = S[i]
        d[i][s].add(index)

# 一致していてほしいM-2文字
strings: list[str] = []


def dfs(string: str):
    if len(string) == M - 2:
        strings.append(string)
        return
    for s in alphabets:
        dfs(string + s)


dfs("")
print(strings)

for string in strings:
    # 一致していてほしいM-2文字
    for indice in combinations(range(M), M - 2):
        # 文字が一致していてほしいM-2箇所のインデックス番号
        #
        # M-2箇所について、M-2文字が等しいやつの集合
        current_set = set(range(N))
        for i in range(M - 2):
            # i:
            s = string[i]
            index = indice[i]
            # 文字列のindex番目がsであるやつ
            current_set &= d[index][s]


print(26**4)
