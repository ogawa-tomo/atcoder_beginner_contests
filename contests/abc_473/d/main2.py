N, K = map(int, input().split())

answers: list[list[int]] = []


def func(current_list: list[int], current_value: int):
    # print(current_list)
    length = len(current_list)
    coefficient = length + 1

    if length == N - 1:
        r = (K - current_value) % coefficient
        if r == 0:
            k = (K - current_value) // coefficient
            next_list = current_list.copy()
            next_list.append(k)
            answers.append(next_list)
        return

    # これだとTLE
    # if length == N:
    #     if current_value == K:
    #         answers.append(current_list)
    #     return

    max_k = (K - current_value) // coefficient
    for k in range(max_k + 1):
        next_list = current_list.copy()
        next_list.append(k)
        next_value = current_value + coefficient * k
        func(next_list, next_value)


func([], 0)

# print(answers)
for answer in answers:
    print(*answer)
