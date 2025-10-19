# TLE
import math


def f(x: int, y: int):
    return int("".join([str(x), str(y)]))


# candidateのうちCの部分
def C_part(C: int, candidate: int):
    if len(str(candidate)) < len(str(C)):
        return False
    return int(str(candidate)[: len(str(C))])


# candidateのうちC+xの部分
def C_x_part(C: int, candidate: int):
    if len(str(candidate)) < len(str(C)):
        return False
    string = str(candidate)[len(str(C)) :]
    if string[0] == "0":
        return False
    return int(string)


# max_value以下で、Cで始まる平方数
def squares_starts_with(C: int, max_value: int):
    values: list[int] = []
    # Cにk桁足したときの平方数
    for k in range(1, 1000):
        min_ = C * 10**k
        max_ = C * 10**k + int("9" * k)
        # print(min_, max_)
        if min_ > max_value:
            break
        min_sqrt = math.ceil(math.sqrt(min_))
        max_sqrt = math.floor(math.sqrt(max_))
        for sqrt in range(min_sqrt, max_sqrt + 1):  # このループを回した時点で時間切れ
            values.append(sqrt**2)
    return values


T = int(input())
for _ in range(T):
    C, D = map(int, input().split())
    f_min = f(C, C + 1)
    f_max = f(C, C + D)
    # sq_root_min = math.ceil(math.sqrt(f_min))
    # sq_root_max = math.floor(math.sqrt(f_max))
    # print(f_min, f_max, sq_root_min, sq_root_max)
    # print(C, D)
    answer = 0
    candidates = squares_starts_with(C, f_max)
    print(candidates)
    for candidate in candidates:
        # candidate = sq_root**2
        # print(candidate)
        # これが、f(C, C+x)で表せるか？
        # print(C_part(C, candidate))
        if C != C_part(C, candidate):
            continue
        # print("candidate", candidate)
        c_x_part = C_x_part(C, candidate)
        # print("c_x_part", c_x_part)
        if not c_x_part:
            continue
        x = c_x_part - C
        if 1 <= x and x <= D:
            # print(candidate)
            answer += 1
    print(answer)
