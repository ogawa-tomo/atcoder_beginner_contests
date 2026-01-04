# RE
from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))


# num_dict[n]: 値がnであるようなインデックスのリスト
num_dict: defaultdict[int, list[int]] = defaultdict(list)
for i in range(N):
    a = A[i]
    num_dict[a].append(i + 1)

# print(num_dict)


def num_of_smaller(num_list: list[int], num: int):
    ok = -1
    ng = len(num_list)
    while ng - ok > 1:
        mid = (ng + ok) // 2
        if num_list[mid] < num:
            ok = mid
        else:
            ng = mid
    return ok + 1


print(num_dict)
answer = 0
for aj in num_dict:
    if aj % 5 != 0:
        continue
    ai = (aj // 5) * 3
    ak = (aj // 5) * 7
    print(aj)

    # ここでdefaultdictを操作してしまっている。defaultdictのkeyでループを回しているので、エラーになってしまう
    i_list = num_dict[ai][:]
    j_list = num_dict[aj][:]
    k_list = num_dict[ak][:]
    print("fuga")
    if not i_list or not k_list or not j_list:
        continue
    print("hoge")
    # print(ai, aj, ak)
    # print(i_list, j_list, k_list)
    for j in j_list:
        # ajより小さいai, ak
        i_num_of_smaller_j = num_of_smaller(i_list, j)
        k_num_of_smaller_j = num_of_smaller(k_list, j)

        answer += i_num_of_smaller_j * k_num_of_smaller_j
        answer += (len(i_list) - i_num_of_smaller_j) * (
            len(k_list) - k_num_of_smaller_j
        )

print(answer)
