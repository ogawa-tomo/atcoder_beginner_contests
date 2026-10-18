class CumulativeSum:
    def __init__(self, _list: list[int]):
        self._list = _list
        total = 0
        self.cumulative_sum_list: list[int] = []
        for elem in self._list:
            total += elem
            self.cumulative_sum_list.append(total)

    def sum(self, index: int):
        if index == -1:
            return 0
        return self.cumulative_sum_list[index]

    def range_sum(self, left_index: int, right_index: int):
        return self.sum(right_index) - self.sum(left_index - 1)


N, Q = map(int, input().split())
A = list(map(int, input().split()))

# cum_sum_list[i]: A0からAiまでの和
cum_sum_list: list[int] = []
current = 0
for a in A:
    current += a
    cum_sum_list.append(current)

# print(cum_sum_list)
cum_sum = CumulativeSum(cum_sum_list)
cum_sum_A = CumulativeSum(A)


# 指定されたiが所属するセクションの番号を返す
def section(index: int):
    ok = 0
    ng = N
    while (ng - ok) > 1:
        mid = (ok + ng) // 2
        if index >= mid * (mid + 1) // 2:
            ok = mid
        else:
            ng = mid
    return ok


def section_start(section_num: int):
    return section_num * (section_num + 1) // 2


def section_end(section_num: int):
    return section_start(section_num + 1) - 1


for _ in range(Q):
    left, right = map(int, input().split())
    left -= 1
    right -= 1
    left_section = section(left)
    right_section = section(right)
    # print(left, right)
    # print(left_section, right_section)

    left_section_start = section_start(left_section)
    left_section_end = section_end(left_section)
    right_section_start = section_start(right_section)
    right_section_end = section_end(right_section)

    # print(left_section_start, left_section_end)
    # print(right_section_start, right_section_end)

    if left_section == right_section:
        start = left - left_section_start
        end = right - right_section_start

        print(cum_sum_A.range_sum(start, end))
    else:
        answer = 0

        left_start = left - left_section_start
        left_end = left_section_end - left_section_start
        answer += cum_sum_A.range_sum(left_start, left_end)

        # right_start = right_section_start
        right_end = right - right_section_start
        answer += cum_sum_A.range_sum(0, right_end)

        start_section = left_section + 1
        end_section = right_section - 1
        if start_section <= end_section:
            answer += cum_sum.range_sum(start_section, end_section)

        print(answer)
