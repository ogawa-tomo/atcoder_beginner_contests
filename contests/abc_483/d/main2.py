# AC
class Move:
    def __init__(
        self, start: int, goal: int, before_min_x: int, before_max_x: int
    ) -> None:
        self.start = start
        self.goal = goal
        # この動きのスタート地点を含め、この動きの前での最小値と最大値
        self.before_min_x = before_min_x
        self.before_max_x = before_max_x
        # この動きのスタートを0としたとき、スタートを含めず、その後の最小値と最大値
        self.after_min_x = 0
        self.after_max_x = 0

    @property
    def move(self):
        return self.goal - self.start

    def __repr__(self) -> str:
        return str((self.after_min_x, self.after_max_x))


N = int(input())
A = list(map(int, input().split()))
moves: list[Move] = []
x = 0
before_min_x = 0
before_max_x = 0
min_x = 0
max_x = 0
for a in A:
    before_min_x = min(before_min_x, x)
    before_max_x = max(before_max_x, x)
    # print(before_min_x, before_max_x)
    start = x
    x += a
    goal = x
    move = Move(start, goal, before_min_x, before_max_x)
    moves.append(move)

    min_x = min(min_x, x)
    max_x = max(max_x, x)

moves.reverse()
after_min_x = 0
after_max_x = 0
x = 0
for move in moves:
    after_min_x += move.move
    after_max_x += move.move
    move.after_min_x = after_min_x
    move.after_max_x = after_max_x
    after_min_x = min(after_min_x, 0)
    after_max_x = max(after_max_x, 0)

moves.reverse()

answer = max_x - min_x + 1
for move in moves:
    min_x = min(move.before_min_x, move.start + move.after_min_x - 2 * move.move)
    max_x = max(move.before_max_x, move.start + move.after_max_x - 2 * move.move)

    answer = max(answer, max_x - min_x + 1)

print(answer)
