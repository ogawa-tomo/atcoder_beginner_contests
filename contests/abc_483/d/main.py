# やめた
class Move:
    def __init__(
        self, min_num: int, max_num: int, total_move: int, start_x: int, result_x: int
    ) -> None:
        self.min_num = min_num
        self.max_num = max_num
        self.start_x = start_x
        self.total_move = total_move
        self.result_x = result_x

    def __repr__(self) -> str:
        return str((self.min_num, self.max_num, self.total_move, self.result_x))


N = int(input())
A = list(map(int, input().split()))

moves: list[Move] = []
min_x = 0
max_x = 0
x = 0
i = 0
max_moved_i = 0  # 移動のうち、最大値に達したものの番号
min_moved_i = 0
while i < N:
    a = A[i]
    org_x = x
    x += a
    min_num = a
    max_num = a

    if a > 0:
        # 正である限り移動
        while i + 1 < N and A[i + 1] > 0:
            i += 1
            min_num = min(min_num, A[i])
            max_num = max(max_num, A[i])
            x += A[i]
    else:
        while i + 1 < N and A[i + 1] < 0:
            i += 1
            min_num = min(min_num, A[i])
            max_num = max(max_num, A[i])
            x += A[i]

    move = Move(min_num, max_num, x - org_x, org_x, x)
    moves.append(move)

    min_x = min(min_x, x)
    max_x = max(max_x, x)
    # if x <= min_x:
    #     min_moved_i = len(moves) - 1
    # if x >= max_x:
    #     max_moved_i = len(moves) - 1

    i += 1

# 最終的なx
result_x = x

print(moves)
print(min_x)
print(max_x)

answer = max_x - min_x + 1

moves.reverse()
current_x = result_x
current_min_x = result_x
current_max_x = result_x
for move in moves:
    current_min_x = min(current_min_x, move.result_x, move.start_x)
    current_max_x = max(current_max_x, move.result_x, move.start_x)

    min_x = min(move.start_x, move.result_x, current_min_x - move.max_num * 2)
    max_x = max(move.start_x, move.result_x, current_max_x - move.min_num * 2)

    answer = max(answer, max_x - min_x + 1)

print(answer)


# トータルで右に動くとき
# if move.total_move > 0:
#     if move.min_num < 0:
