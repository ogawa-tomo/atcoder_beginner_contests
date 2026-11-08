N = int(input())


def question(left: int, right: int):
    print("?", left, right, flush=True)
    return input() == "Yes"


answer = 0
right = 1
for left in range(1, N):
    if right < left:
        right = left

    while right + 1 <= N and question(left, right + 1):
        right += 1

    answer += right - left

print("!", answer, flush=True)
exit()
