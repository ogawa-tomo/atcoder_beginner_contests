from collections import defaultdict


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


class Piece:
    def __init__(self, r: int, c: int) -> None:
        self.r = r
        self.c = c
        self.row_index = 0
        self.column_index = 0


H, W, N, Q = map(int, input().split())

rows: set[int] = set()
columns: set[int] = set()
pieces: list[Piece] = []
for _ in range(N):
    r, c = map(int, input().split())
    r -= 1
    c -= 1
    rows.add(r)
    columns.add(c)
    piece = Piece(r, c)
    pieces.append(piece)

row_list = list(rows)
row_list.sort()
column_list = list(columns)
column_list.sort()
# print(row_list, column_list)

# column_index[c]: c列目の、column_listのインデックス
# column_index: defaultdict[int, int] = defaultdict(int)
column_index: dict[int, int] = dict()
for i in range(len(column_list)):
    c = column_list[i]
    column_index[c] = i
row_index: dict[int, int] = dict()
for i in range(len(row_list)):
    r = row_list[i]
    row_index[r] = i

# row_piece_num[row_index]: r_index列目の駒の数
row_piece_num = [0] * len(row_list)
column_piece_num = [0] * len(column_list)
for piece in pieces:
    row_i = row_index[piece.r]
    row_piece_num[row_i] += 1
    column_i = column_index[piece.c]
    column_piece_num[column_i] += 1

# print(row_piece_num)
# print(column_piece_num)

cum_sum_row = CumulativeSum(row_piece_num)
cum_sum_column = CumulativeSum(column_piece_num)


def get_min_column_index(c: int):
    if c in column_index:
        return column_index[c]
    ng = -1
    ok = len(column_list)
    while ok - ng > 1:
        mid = (ok + ng) // 2
        if c < column_list[mid]:
            ok = mid
        else:
            ng = mid
    return ok


def get_min_row_index(r: int):
    if r in row_index:
        return row_index[r]
    ng = -1
    ok = len(row_list)
    while ok - ng > 1:
        mid = (ok + ng) // 2
        if r < row_list[mid]:
            ok = mid
        else:
            ng = mid
    return ok


def get_max_column_index(c: int):
    if c in column_index:
        return column_index[c]
    ok = -1
    ng = len(column_list)
    while ng - ok > 1:
        mid = (ng + ok) // 2
        if column_list[mid] < c:
            ok = mid
        else:
            ng = mid
    return ok


def get_max_row_index(r: int):
    if r in row_index:
        return row_index[r]
    ok = -1
    ng = len(row_list)
    while ng - ok > 1:
        mid = (ng + ok) // 2
        if row_list[mid] < r:
            ok = mid
        else:
            ng = mid
    return ok


for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        u = q[1]
        d = q[2]
        u -= 1
        d -= 1
        # min_row_i = row_index[u]
        min_row_i = get_min_row_index(u)
        # max_row_i = row_index[d]
        max_row_i = get_max_row_index(d)
        # print(u, d)
        # print(min_row_i, max_row_i)
        if min_row_i >= len(row_list):
            print(0)
        elif max_row_i < 0:
            print(0)
        elif max_row_i < min_row_i:
            print(0)
        else:
            answer = cum_sum_row.range_sum(min_row_i, max_row_i)
            print(answer)
    elif q[0] == 2:
        l = q[1]
        r = q[2]
        l -= 1
        r -= 1
        # min_col_i = column_index[l]
        min_col_i = get_min_column_index(l)
        # max_col_i = column_index[r]
        max_col_i = get_max_column_index(r)
        if min_col_i >= len(column_list):
            print(0)
        elif max_col_i < 0:
            print(0)
        elif max_col_i < min_col_i:
            print(0)
        else:
            # print(l, r, min_col_i, max_col_i)
            answer = cum_sum_column.range_sum(min_col_i, max_col_i)
            print(answer)
