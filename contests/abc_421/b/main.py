x, y = map(int, input().split())


def f(x: int):
    string: list[str] = list(str(x))
    string.reverse()
    value = "".join(string)
    return int(value)


# print(f(10))

A: list[int] = []
A.append(x)
A.append(y)
for i in range(2, 10):
    A.append(f(A[i - 1] + A[i - 2]))
print(A[9])
