import math

N, K = map(int, input().split())
S = list(input())

# print(S)

# 確定させる
for i in range(N):
    if S[i] != "?":
        continue
    if i > 0 and S[i - 1] == "o":
        S[i] = "."
        continue
    if i < N - 1 and S[i + 1] == "o":
        S[i] = "."
        continue

# print(S)
o_num = 0
q_num = 0
for s in S:
    if s == "o":
        o_num += 1
    elif s == "?":
        q_num += 1
add_o_num = K - o_num
# print(S)
# print(q_num, add_o_num)
# q_num個の?のうち、add_o_num個をoに置き換える
# is_all_o = q_num == add_o_num


# ?の島と、そのキャパシティを数える
class QLand:
    def __init__(self, start_index: int, length: int):
        self.start_index = start_index
        self.length = length

    def capacity(self):
        return math.ceil(self.length / 2)

    def __repr__(self):
        return str([self.start_index, self.length])


q_lands: list[QLand] = []
in_land = False
current_length = 0
for i in range(N):
    if S[i] == "?":
        if i == N - 1:
            if in_land:
                current_length += 1
                q_lands.append(QLand(i - current_length + 1, current_length))
            else:
                q_lands.append(QLand(i, 1))
        elif in_land:
            current_length += 1
        else:
            in_land = True
            current_length = 1
    else:
        if in_land:
            in_land = False
            q_lands.append(QLand(i - current_length, current_length))
        else:
            pass
# print(S)
# print(q_lands)
q_land_capacity = 0
for q_land in q_lands:
    q_land_capacity += q_land.capacity()

is_full_capacity = q_land_capacity == add_o_num
# print(S)
# print(q_land_capacity)
# print(add_o_num)

T: list[str] = []
i = 0
# for i in range(N):
curernt_q_lands_index = 0
while i < N:
    if S[i] == "o":
        T.append("o")
        i += 1
        continue
    elif S[i] == ".":
        T.append(".")
        i += 1
        continue
    # ?のとき
    if add_o_num == 0:
        T.append(".")
        i += 1
        continue
    q_land = q_lands[curernt_q_lands_index]
    for j in range(q_land.length):
        if not is_full_capacity:
            T.append("?")
        else:
            if q_land.length % 2 == 0:
                T.append("?")
            else:
                if j % 2 == 0:
                    T.append("o")
                else:
                    T.append(".")

        i += 1
    curernt_q_lands_index += 1

print("".join(T))
