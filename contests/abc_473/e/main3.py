# AC
N, K = map(int, input().split())
A = list(map(int, input().split()))

answer = 0
reminders: set[int] = {0}
value = 0
for a in A:
    value += a
    value %= K
    # print(a, value)
    if value in reminders:
        # print("answer")
        answer += 1
        reminders = {0}
        value = 0
    else:
        reminders.add(value)

print(answer)
