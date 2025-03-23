# これはTLE。Nで二重ループしてるから
N, X, Y = map(int, input().split())
S = list(input())

# print(S)

grids: list[list[bool]] = []
for _ in range(2 * N + 1):
    row = [False] * (2 * N + 1)
    grids.append(row)
# print(grids)

origin_x = N
origin_y = N
grids[origin_x][origin_y] = True
# X += N
# Y += N
# print(X, Y)


# for row in grids:
#     print(row)

answers: list[str] = []
for s in S:
    if s == "N":
        # 東風
        # current_origin_r += 1
        origin_x += 1
    if s == "W":
        # 北風
        # current_origin_c += 1
        origin_y += 1
    if s == "S":
        # 西風
        # current_origin_r -= 1
        origin_x -= 1
    if s == "E":
        # 南風
        # current_origin_c -= 1
        origin_y -= 1
    grids[origin_x][origin_y] = True

    # for row in grids:
    #     print(row)
    # print(current_origin_c, current_origin_r)
    # exit()

    # if grids[X - origin_x][Y - origin_y]:
    if grids[origin_x + X][origin_y + Y]:
        answers.append("1")
    else:
        answers.append("0")
# for row in grids:
#     print(row)

print("".join(answers))
