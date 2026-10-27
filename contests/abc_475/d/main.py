from collections import defaultdict
import math


def is_prime(x):
    if x <= 1:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


S = input()

indice_by_alphabet: defaultdict[str, list[int]] = defaultdict(list)
for i in range(len(S)):
    s = S[i]
    indice_by_alphabet[s].append(i)

same_indice: defaultdict[int, list[int]] = defaultdict(list)
for i in range(len(S)):
    s = S[i]
    same_indice[i] = indice_by_alphabet[s]

# print(same_indice)


def dfs(current: list[int], index: int, nums: set[int]):
    if index == len(S):
        # print(current)
        if current[0] == 0:
            return
        number = int("".join(str(c) for c in current))
        if is_prime(number):
            print(number)
            exit()
        return

    if current[index] != -1:
        dfs(current, index + 1, nums)
    else:
        for num in nums:
            new_nums = nums.copy()
            new_nums.remove(num)
            new_current = current.copy()
            for i in same_indice[index]:
                new_current[i] = num
            dfs(new_current, index + 1, new_nums)


dfs([-1] * len(S), 0, {0, 1, 2, 3, 4, 5, 6, 7, 8, 9})
print(-1)

# print(is_prime(81817))
# print(9 * 9 * 8 * 7 * 6 * 5 * 4)
