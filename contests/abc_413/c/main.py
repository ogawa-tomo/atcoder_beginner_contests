# 難しく考えすぎか…？
Q = int(input())
A: list[int] = []


class NumSet:
    def __init__(self, num: int, value: int):
        self.num = num
        self.value = value

    def __repr__(self):
        return f"[{self.value}, {self.num}]"


class NumSetList:
    def __init__(self) -> None:
        self.num_set_list: list[NumSet] = []
        # num_set_num[i]: i番目まででいくつの要素があるか
        self.num_set_num: list[int] = []
        # num_set_sum[i]: i番目までの合計
        self.num_set_sum: list[int] = []
        self.length = 0

    def append(self, num_set: NumSet):
        self.num_set_list.append(num_set)
        self.num_set_num.append(num_set.num)
        if self.length == 0:
            self.num_set_sum.append(num_set.num * num_set.value)
        else:
            self.num_set_sum.append(self.num_set_sum[-1] + num_set.num * num_set.value)
        self.length += 1

    # kが与えられたとき、要素数がk以上となる最小のインデックス
    def find_index(self, k):
        ng = -1
        ok = self.length
        while ng - ok > 1:
            mid = (ok + ng) // 2
            if self.num_set_num[mid] >= k:
                ok = mid
            else:
                ng = mid
        return ok

    # kが与えられたとき、そこまでの和を求める
    def sum_by_index(self, k):
        index = self.find_index(k)
        answer = 0
        if index != -1:
            answer += self.num_set_sum[index]
        answer += (self.num_set_num[index] - k) * self.num_set_list[index].value
        return answer


num_set_list = NumSetList()
current_index = 0
for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        c = q[1]
        x = q[2]
        num_set_list.append(NumSet(c, x))
    # elif q[0] == 2:
    #     k = q[1] - 1

    #     next_index = current_index + k
    #     print(sum_by_index(next_index) - sum_by_index(current_index))
    #     current_index = next_index
