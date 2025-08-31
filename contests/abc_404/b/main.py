N = int(input())

S: list[list[str]] = []
for _ in range(N):
    row = list(input())
    S.append(row)
T: list[list[str]] = []
for _ in range(N):
    row = list(input())
    T.append(row)

# print(S)
# print(T)


def rotated(grids: list[list[str]]):
    result: list[list[str]] = []
    for i in range(N):
        row: list[str] = []
        for j in range(N):
            row.append(grids[N - j - 1][i])
        result.append(row)
    return result


def diff_count(grids1: list[list[str]], grids2: list[list[str]]):
    result = 0
    for i in range(N):
        for j in range(N):
            if grids1[i][j] != grids2[i][j]:
                result += 1
    return result


def rotate_effect(S: list[list[str]], T: list[list[str]], rotate_num):
    before = diff_count(S, T)
    rotated_s = rotated(S)
    for _ in range(rotate_num - 1):
        rotated_s = rotated(rotated_s)
    after = diff_count(rotated_s, T)
    return before - after


answer = 0
already_rotated = False
while True:
    diff = diff_count(S, T)
    if diff <= 1:
        print(answer + diff)
        exit()

    one_rotate_effect = rotate_effect(S, T, 1)
    two_rotate_effect = rotate_effect(S, T, 2)
    three_rotate_effect = rotate_effect(S, T, 3)
    # print(one_rotate_effect, two_rotate_effect, three_rotate_effect)
    if one_rotate_effect >= 2:
        S = rotated(S)
        answer += 1
        continue
    elif two_rotate_effect >= 3:
        S = rotated(rotated(S))
        answer += 2
        continue
    elif three_rotate_effect >= 4:
        S = rotated(rotated(rotated(S)))
        answer += 3
        continue
    # already_rotated = True
    print(answer + diff)
    exit()
