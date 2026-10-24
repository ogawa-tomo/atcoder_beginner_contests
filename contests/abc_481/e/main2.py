from fractions import Fraction
import sys


class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

        if x == 0:
            self.tan = Fraction(-sys.maxsize, 1)
        else:
            self.tan = Fraction(self.y, self.x)

    def __repr__(self) -> str:
        return str((self.x, self.y))


T = int(input())

for _ in range(T):
    N = int(input())

    points: list[Point] = []
    x_plus_points_num = 0
    x_minus_points_num = 0
    x_zero_point: Point | None = None
    for _ in range(N):
        x, y = map(int, input().split())
        point = Point(x, y)
        points.append(point)
        if x > 0:
            x_plus_points_num += 1
        elif x < 0:
            x_minus_points_num += 1
        else:
            x_zero_point = point

    points.sort(key=lambda p: p.tan)

    # 直線がx = 0のときの答え
    answer = max(x_plus_points_num, x_minus_points_num)
    if x_zero_point is not None:
        answer += 1
        # 直線がx = 0からちょっとだけ回転したときの答え
        if x_zero_point.y < 0:
            x_minus_points_num += 1
        else:
            x_plus_points_num += 1
        answer = max(answer, max(x_plus_points_num, x_minus_points_num))

    for point in points:
        if point == x_zero_point:
            continue
        # 直線がこのポイントからちょっとだけ回転したときの答え
        if point.x > 0:
            x_plus_points_num -= 1
            x_minus_points_num += 1
        else:
            x_plus_points_num += 1
            x_minus_points_num -= 1
        answer = max(answer, max(x_plus_points_num, x_minus_points_num))

    print(answer)
