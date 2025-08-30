N = int(input())
S = list(input())

print(S)
a_indice: list[int] = []
b_indice: list[int] = []
for i, s in enumerate(S):
    if s == "A":
        a_indice.append(i)
    else:
        b_indice.append(i)
print(a_indice, b_indice)
a_index = 0
b_index = 0

answer = 0
for i in range(2 * N - 1):
    s = S[i]
    next_s = S[i + 1]
    # if s != next_s:
    #     continue
    if s == "A":
        a_index += 1
        if s != next_s:
            continue
        S[i + 1] = "B"
        next_b_index = b_indice[b_index]
        S[next_b_index] = "A"
        answer += next_b_index - i + 1
        b_index += 1
    elif s == "B":
        b_index += 1
        if s != next_s:
            continue
        S[i + 1] = "A"
        next_a_index = a_indice[a_index]
        S[next_a_index] = "B"
        answer += next_a_index - i + 1
        a_index += 1
print(answer)
