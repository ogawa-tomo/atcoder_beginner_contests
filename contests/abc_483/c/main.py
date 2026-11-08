from collections import defaultdict

N, M = map(int, input().split())


# first_choise[i]: iを第1候補とした票数
first_choise: defaultdict[int, int] = defaultdict(int)
# second_choise[i]: iを第2候補とした票数
# second_choise: defaultdict[int, int] = defaultdict(int)

# instead_choise[i][j]: iが辞退したときにjに入る票の数
instead_choise: dict[int, dict[int, int]] = dict()
for i in range(1, N + 1):
    instead_choise[i] = dict()
for _ in range(M):
    a, b = map(int, input().split())
    first_choise[a] += 1
    # second_choise[b] += 1
    if b in instead_choise[a]:
        instead_choise[a][b] += 1
    else:
        instead_choise[a][b] = 1

# print(instead_choise)
top_candidates: set[int] = set()
top_num = max(first_choise.values())  # 1位の票数
top_candidate = 0
for i in range(1, N + 1):
    if first_choise[i] == top_num:
        top_candidate = i
        break

second_top_num = 0
second_top_candidate = 0
for i in range(1, N + 1):
    if i == top_candidate:
        continue
    if first_choise[i] == top_num:
        second_top_candidate = i
        second_top_num = top_num
        break
    if first_choise[i] > second_top_num:
        second_top_candidate = i
        second_top_num = first_choise[i]
# print(top_candidate, top_num)
# print(second_top_candidate, second_top_num)

for k in range(1, N + 1):
    # print("k", k)
    if k == top_candidate:
        current_candidate = second_top_candidate
        current_top_num = second_top_num
    else:
        current_candidate = top_candidate
        current_top_num = top_num

    # kが辞退したときに各候補者に増える票
    for plus_candidate in instead_choise[k]:
        # print("plus_candidate", plus_candidate)
        # print("plus_num", instead_choise[k][plus_candidate])
        plused_votes = first_choise[plus_candidate] + instead_choise[k][plus_candidate]
        if plused_votes > current_top_num or (
            plused_votes == current_top_num and plus_candidate < current_candidate
        ):
            current_candidate = plus_candidate
            current_top_num = plused_votes

    print(current_candidate)
