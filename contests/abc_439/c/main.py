# TLE
import math

N = int(input())


def is_good(n: int):
    sqrt = math.isqrt(n)
    # start = sqrt
    matches: int | None = None
    while True:
        other_sqrt = math.sqrt(n - sqrt**2)
        # print(sqrt, other_sqrt)
        if other_sqrt >= sqrt:
            break
        if other_sqrt.is_integer():
            candid = math.isqrt(n - sqrt**2)
            if candid == 0:
                pass
            elif matches is None:
                matches = candid
            else:
                return False
        sqrt -= 1
    # print(matches)
    if matches is None:
        return False
    else:
        return True


# print(is_good(4))
answers = []
for i in range(1, N + 1):
    if is_good(i):
        answers.append(i)

print(len(answers))
print(*answers)

# print(math.isqrt(37))
# for i in range(N):
#     sqrt = math.isqrt(i)
