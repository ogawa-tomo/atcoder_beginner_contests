N, M, Sx, Sy = map(int, input().split())


class House:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.visited = False


houses: list[House] = []
houses_x: dict[int, list[House]] = {}  # houses_x[x]: x座標がxにある家のリスト
houses_y: dict[int, list[House]] = {}  # houses_y[y]: y座標がyにある家
for _ in range(N):
    x, y = map(int, input().split())
    house = House(x, y)
    houses.append(house)
    if x in houses_x:
        houses_x[x].append(house)
    else:
        houses_x[x] = [house]
    if y in houses_y:
        houses_y[y].append(house)
    else:
        houses_y[y] = [house]
# print(houses_x)

num_visited = 0
for _ in range(M):
    D, c = input().split()
    C = int(c)

    if D == "U":
        # x == Sx, Sy < y <= Sy + C にある家を数える
        if Sx in houses_x:
            houses_in_sx = sorted(houses_x[Sx], key=lambda house: house.x)
            # 二分探索
            ok = 10 ** (-9)
            ng = 10**9

            for house in houses_in_sx:
                if not house.visited and Sy < house.y and house.y <= Sy + C:
                    house.visited = True
                    num_visited += 1
        Sy += C
    elif D == "D":
        # x == Sx, Sy - C <= y < Syにある家を数える
        if Sx in houses_x:
            for house in houses_x[Sx]:
                if not house.visited and Sy - C <= house.y and house.y < Sy:
                    house.visited = True
                    num_visited += 1
        Sy -= C
    elif D == "L":
        # y == Sy, Sx - C <= x < Sxにある家
        if Sy in houses_y:
            for house in houses_y[Sy]:
                if not house.visited and Sx - C <= house.x and house.x < Sx:
                    house.visited = True
                    num_visited += 1
        Sx -= C
    elif D == "R":
        # y == Sy, Sx < x <= Sx + C にある家
        if Sy in houses_y:
            for house in houses_y[Sy]:
                if not house.visited and Sx < house.x and house.x <= Sx + C:
                    house.visited = True
                    num_visited += 1
        Sx += C


print(Sx, Sy, num_visited)
