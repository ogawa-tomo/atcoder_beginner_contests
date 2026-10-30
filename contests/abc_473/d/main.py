# TLE
N, K = map(int, input().split())

answers: list[list[int]] = []


def func(current_list: list[int], current_value: int, current_index: int):
    # print(current_list)
    if current_index == 0:
        if current_value == 0:
            answers.append(current_list)
        return
        #     return current_list
        # else:
        #     return None

    if current_value < 0:
        return

    # ここのループが長過ぎるのかな？
    for i in range(current_value + 1):
        new_list = current_list.copy()
        new_list.append(i)
        new_index = current_index - 1
        new_value = current_value - i * current_index
        func(new_list, new_value, new_index)


func([], K, N)

for answer in answers:
    answer.reverse()

#
answers.sort()
for answer in answers:
    print(*answer)
# print(answers)
