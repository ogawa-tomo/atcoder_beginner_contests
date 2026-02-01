N, T = map(int, input().split())
A = list(map(int, input().split()))

answer = 0
state = "open"  # "open" or "close"
last_open = 0  # 最後に開いた時刻
last_close = 0  # 最後に閉じた時刻
for a in A:
    if a <= last_open:
        continue
    answer += a - last_open
    last_close = a
    last_open = a + 100
# print(last_open)
if last_open < T:
    answer += T - last_open
print(answer)
