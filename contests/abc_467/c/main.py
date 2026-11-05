# WA
N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ok_list: list[int] = []
for i in range(N - 1):
    if (A[i] + A[i + 1]) % 2 == B[i]:
        ok_list.append(True)
    else:
        ok_list.append(False)

# print(ok_list)


def get_answer(ok_list: list[int]):
    answer = 0
    for i in range(N - 1):
        ok = ok_list[i]
        if ok:
            continue

        answer += 1
        if i < N - 2:
            ok_list[i + 1] = not ok_list[i + 1]

    return answer


ok_list.reverse()
ok_list2 = ok_list.copy()
ok_list2[0] = not ok_list2[0]

answer1 = get_answer(ok_list)
answer2 = get_answer(ok_list2)

print(min(answer1, answer2))
