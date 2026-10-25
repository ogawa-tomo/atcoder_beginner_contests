# AC
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


N, M, K = map(int, input().split())
X, Y = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()

# needed_k_bill_list[i]: i個目のドリンクを買うときに必要なKドル札の枚数
needed_k_bill_list: list[int] = []
# change_list[i]: i個目のドリンクを買ったときのお釣り
change_list: list[int] = []
for b in B:
    num = b // K
    amari = b % K
    if amari != 0:
        num += 1
        change = K - amari
    else:
        change = 0
    needed_k_bill_list.append(num)
    change_list.append(change)

cum_sum_k_bills = CumulativeSum(needed_k_bill_list)
cum_sum_change = CumulativeSum(change_list)

cum_sum_dessert = CumulativeSum(A)


# moneyでデザートを買える数
def get_buyable_desserts_num(money: int):
    ok = -1
    ng = N
    while ng - ok > 1:
        mid = (ng + ok) // 2
        if cum_sum_dessert.range_sum(0, mid) <= money:
            ok = mid
        else:
            ng = mid
    return ok + 1


# ドリンクを買わずにデザートを買う
answer = get_buyable_desserts_num(X + Y * K)
for i in range(M):
    # drinkをi個目まで買う
    needed_k_bills = cum_sum_k_bills.range_sum(0, i)
    if needed_k_bills > Y:
        break

    # おつり
    change = cum_sum_change.range_sum(0, i)

    # 残ったお金でデザートを買う
    remaining_money = X + change + (Y - needed_k_bills) * K
    buyable_desserts_num = get_buyable_desserts_num(remaining_money)

    answer = max(answer, i + 1 + buyable_desserts_num)

print(answer)
