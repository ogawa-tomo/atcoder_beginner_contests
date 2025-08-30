N = int(input())
S = list(input())

first_char = S[0]
first_char_indice: list[int] = []

for i, s in enumerate(S):
    if s == first_char:
        first_char_indice.append(i)


answer_indice1 = [i * 2 for i in range(N)]
answer_indice2 = [i * 2 + 1 for i in range(N)]
# print(answer_indice1)
# print(answer_indice2)
answer1 = 0
answer2 = 0
for i in range(N):
    first_char_index = first_char_indice[i]
    answer1_index = answer_indice1[i]
    answer2_index = answer_indice2[i]
    answer1 += abs(first_char_index - answer1_index)
    answer2 += abs(first_char_index - answer2_index)

print(min(answer1, answer2))
