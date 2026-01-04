N = int(input())


def calc(n: int):
    nums = list(map(int, list(str(n))))
    result = 0
    for num in nums:
        result += num**2
    return result


# print(calc(2026))
n = N
emerged: set[int] = set()
while True:
    n = calc(n)
    if n == 1:
        print("Yes")
        exit()
    if n in emerged:
        print("No")
        exit()
    emerged.add(n)
