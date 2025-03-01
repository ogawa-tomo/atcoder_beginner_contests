import sys

sys.setrecursionlimit(12000000)

S = list(input())


def is_colourful(string: list[str]):
    if len(string) == 2:
        if string[0] == "(" and string[1] == ")":
            return True
        if string[0] == "[" and string[1] == "]":
            return True
        if string[0] == "<" and string[1] == ">":
            return True
        return False
    converted: list[str] = []
    length = len(string)
    i = 0
    kakko_exists = False
    while True:
        if i >= length:
            break
        if string[i] == "(" and string[i + 1] == ")":
            i += 2
            kakko_exists = True
            continue
        if string[i] == "[" and string[i + 1] == "]":
            i += 2
            kakko_exists = True
            continue
        if string[i] == "<" and string[i + 1] == ">":
            i += 2
            kakko_exists = True
            continue
        converted.append(string[i])
        i += 1
    if not kakko_exists:
        return False
    return is_colourful(converted)


if is_colourful(S):
    print("Yes")
else:
    print("No")
