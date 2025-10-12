N = int(input())


def f(num: int):
    num_str = str(num)
    # print(list(num_str))
    answer = 0
    for n in num_str:
        answer += int(n)
    return answer


# print(f(563))

A: list[int] = []
for i in range(N + 1):
    if i == 0:
        A.append(1)
        continue
    answer = 0
    for a in A:
        answer += f(a)
    A.append(answer)

print(A[N])
