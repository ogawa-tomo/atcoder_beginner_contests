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


T = int(input())
for _ in range(T):
    C, D = map(int, input().split())
    f_min = f(C, C + 1)
    f_max = f(C, C + D)
    sq_root_min = math.ceil(math.sqrt(f_min))
    sq_root_max = math.floor(math.sqrt(f_max))
    # print(f_min, f_max, sq_root_min, sq_root_max)
    # print(C, D)
    answer = 0
    for sq_root in range(sq_root_min, sq_root_max + 1):
        candidate = sq_root**2
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
