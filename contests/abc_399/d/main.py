# これは落ちる
T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    index_dict: dict[int, list[int]] = {}
    for i, a in enumerate(A):
        if a not in index_dict:
            index_dict[a] = [i]
        else:
            index_dict[a].append(i)

    # print(index_dict)
    # aのカップルが隣合っているか
    def is_neighbors(a):
        indexes = index_dict[a]
        return abs(indexes[1] - indexes[0]) == 1

    answers: set[tuple[int, int]] = set()
    for i, a in enumerate(A):
        indexes = index_dict[a]
        if indexes[0] == i:
            pertner_index = indexes[1]
        else:
            pertner_index = indexes[0]

        # もともと隣り合っているのは無視
        if is_neighbors(a):
            continue
        # パートナーの手前にいるひと
        if pertner_index > 0:
            before_pertner_num = A[pertner_index - 1]
            if not is_neighbors(before_pertner_num):
                # 自分の前
                if i > 0:
                    before_myself_num = A[i - 1]
                    if before_myself_num == before_pertner_num:
                        answers.add((a, before_myself_num))

                # 自分の後ろ
                if i < N - 1:
                    after_myself_num = A[i + 1]
                    if after_myself_num == before_pertner_num:
                        answers.add((a, after_myself_num))
                        continue

        # パートナーの奥にいるひと
        if pertner_index < N - 1:
            after_pertner_num = A[pertner_index + 1]
            if not is_neighbors(after_pertner_num):
                # 自分の前
                if i > 0:
                    before_myself_num = A[i - 1]
                    if before_myself_num == after_pertner_num:
                        answers.add((a, after_pertner_num))
                # 自分の後ろ
                if i < N - 1:
                    after_myself_num = A[i + 1]
                    if after_myself_num == after_pertner_num:
                        answers.add((a, after_pertner_num))
    print(len(answers) // 2)
