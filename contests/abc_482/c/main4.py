from typing import Callable


class CumulativeSum:
    def __init__(self, _list: list[int]):
        self._list = _list
        self.length = len(_list)
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
        if left_index < 0 or self.length <= right_index or right_index < left_index:
            raise
        return self.sum(right_index) - self.sum(left_index - 1)


# 座標圧縮
class Compress:
    def __init__(self, org_list: list[int]) -> None:
        self.org_list = org_list

        self.duplicate_removed_list = org_list.copy()
        self.duplicate_removed_list = list(set(self.duplicate_removed_list))
        self.duplicate_removed_list.sort()

        # もとの数列の値を与えたとき、何番目に大きい値かを返す辞書
        self.rank_by_num: dict[int, int] = dict()
        for i in range(len(self.duplicate_removed_list)):
            v = self.duplicate_removed_list[i]
            self.rank_by_num[v] = i

        # selc.compressed[i]: もとの数列のi番目が、何番目に大きい値か
        self.compressed: list[int] = []
        for v in self.org_list:
            self.compressed.append(self.rank_by_num[v])


def get_duplicate_removed(org_list: list[int]):
    return Compress(org_list).duplicate_removed_list


def get_compressed(org_list: list[int]):
    return Compress(org_list).compressed


def get_rank_by_num(org_list: list[int]):
    return Compress(org_list).rank_by_num


# 二分探索
def most_right_ok(min_i: int, max_i: int, ok_func: Callable[[int], bool]):
    ok = min_i - 1
    ng = max_i + 1
    while ng - ok > 1:
        mid = (ok + ng) // 2
        if ok_func(mid):
            ok = mid
        else:
            ng = mid
    if ok < min_i:
        return None
    return ok


# 二分探索
def most_left_ok(min_i: int, max_i: int, ok_func: Callable[[int], bool]):
    ok = max_i + 1
    ng = min_i - 1
    while ok - ng > 1:
        mid = (ok + ng) // 2
        if ok_func(mid):
            ok = mid
        else:
            ng = mid
    if ok > max_i:
        return None
    return ok


class Piece:
    def __init__(self, c: int, r: int) -> None:
        self.c = c
        self.r = r


H, W, N, Q = map(int, input().split())

rows: list[int] = []
columns: list[int] = []
pieces: list[Piece] = []
for _ in range(N):
    r, c = map(int, input().split())
    r -= 1
    c -= 1
    rows.append(r)
    columns.append(c)
    pieces.append(Piece(c, r))

# あんまり意味がないが、座標圧縮された配列について駒の数の累積和をとる解法

compressed_rows = Compress(rows)
compressed_columns = Compress(columns)

# rank_by_row = get_rank_by_num(rows)
rank_by_row = compressed_rows.rank_by_num
# rank_by_column = get_rank_by_num(columns)
rank_by_column = compressed_columns.rank_by_num

# duplicate_removed_rows = get_duplicate_removed(rows)
duplicate_removed_rows = compressed_rows.duplicate_removed_list
# duplicate_removed_columns = get_duplicate_removed(columns)
duplicate_removed_columns = compressed_columns.duplicate_removed_list

compressed_rows_length = len(duplicate_removed_rows)
compressed_columns_length = len(duplicate_removed_columns)

# pieces_by_compressed_row[r]: 座標圧縮されたrow配列のr番目にある駒の数
pieces_by_compressed_row: list[int] = [0] * compressed_rows_length
pieces_by_compressed_column: list[int] = [0] * compressed_columns_length
for piece in pieces:
    r_index = rank_by_row[piece.r]
    pieces_by_compressed_row[r_index] += 1
    c_index = rank_by_column[piece.c]
    pieces_by_compressed_column[c_index] += 1

# 座標圧縮された配列についての累積和
cum_sum_row = CumulativeSum(pieces_by_compressed_row)
cum_sum_column = CumulativeSum(pieces_by_compressed_column)

for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        u = q[1]
        d = q[2]
        u -= 1
        d -= 1

        # 座標圧縮された配列のインデックスを求める
        min_i = most_left_ok(
            0, compressed_rows_length - 1, lambda i: u <= duplicate_removed_rows[i]
        )
        max_i = most_right_ok(
            0, compressed_rows_length - 1, lambda i: duplicate_removed_rows[i] <= d
        )
        if min_i is None or max_i is None or max_i < min_i:
            print(0)
        else:
            print(cum_sum_row.range_sum(min_i, max_i))

    elif q[0] == 2:
        l = q[1]
        r = q[2]
        l -= 1
        r -= 1

        min_i = most_left_ok(
            0,
            compressed_columns_length - 1,
            lambda i: l <= duplicate_removed_columns[i],
        )
        max_i = most_right_ok(
            0,
            compressed_columns_length - 1,
            lambda i: duplicate_removed_columns[i] <= r,
        )
        if min_i is None or max_i is None or max_i < min_i:
            print(0)
        else:
            print(cum_sum_column.range_sum(min_i, max_i))
