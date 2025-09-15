S = input()


def calc(string):
    if len(string) < 3:
        return 0
    if string[0] != "t" or string[-1] != "t":
        return 0
    t_num = 0
    for s in string:
        if s == "t":
            t_num += 1
    return (t_num - 2) / (len(string) - 2)


# print(calc("ttit"))
t_indice: list[int] = []
for i in range(len(S)):
    if S[i] == "t":
        t_indice.append(i)

answer = 0
for i in t_indice:
    for j in t_indice:
        if i >= j:
            continue
        answer = max(answer, calc(S[i : j + 1]))

print(answer)
