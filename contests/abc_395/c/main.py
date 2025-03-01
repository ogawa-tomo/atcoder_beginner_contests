N = int(input())
A = list(map(int, input().split()))


class Data:
    def __init__(self):
        self.current_start_index = 0
        self.emerged = False
        self.min_range = 0


max_num = 10**6 + 1
# max_num = 10 + 1
d: dict[int, Data] = {}
for i in range(max_num):
    d[i] = Data()

# print(d)
for i, a in enumerate(A):
    data = d[a]
    if not data.emerged:
        data.emerged = True
        data.current_start_index = i
    else:
        data.min_range = i - data.current_start_index + 1
        data.current_start_index = i

answer = 10**7
for data in d.values():
    if data.emerged and data.min_range != 0:
        answer = min(answer, data.min_range)
if answer == 10**7:
    print(-1)
else:
    print(answer)
