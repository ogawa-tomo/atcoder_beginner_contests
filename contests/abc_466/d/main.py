N, M = map(int, input().split())

# column_for_row[r]: r行目に置いてあるコマの列
column_for_row: dict[int, int | None] = dict()
# row_for_column[c]: c列目に置いてあるコマの行
row_for_column: dict[int, int | None] = dict()

for i in range(N):
    column_for_row[i] = None
    row_for_column[i] = None
for _ in range(M):
    r, c = map(int, input().split())
    r -= 1
    c -= 1

    c_for_r = column_for_row[r]
    if c_for_r is not None:
        row_for_column[c_for_r] = None
    r_for_c = row_for_column[c]
    if r_for_c is not None:
        column_for_row[r_for_c] = None

    column_for_row[r] = c
    row_for_column[c] = r

answer = 0
for r in range(N):
    if column_for_row[r] is not None:
        answer += 1

print(answer)
