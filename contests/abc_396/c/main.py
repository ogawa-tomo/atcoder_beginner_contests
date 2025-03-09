N, M = map(int, input().split())
black_values = list(map(int, input().split()))
white_values = list(map(int, input().split()))

black_values.sort(reverse=True)
white_values.sort(reverse=True)
# print(black_values)
# print(white_values)

score = 0
black_index = 0
white_index = 0
while True:
    if black_index >= N:
        break
    if white_index >= M:
        # 黒だけ考える
        black_value = black_values[black_index]
        if black_value >= 0:
            score += black_value
            black_index += 1
            continue
        else:
            break
    if black_index < white_index:
        break
    black_value = black_values[black_index]
    white_value = white_values[white_index]

    # blackが正
    if black_value >= 0:
        # 黒をとる
        score += black_value
        black_index += 1
        # 白が0以上ならとる
        if white_value < 0:
            continue
        score += white_value
        white_index += 1

    # blackが負
    else:
        # 白インデックスのほうが小さい=白だけをとれる
        if black_index > white_index:
            # 白が正なら、取る
            if white_value >= 0:
                score += white_value
                white_index += 1
            # 白が負なら、おわり
            else:
                break
        # 黒インデックスと白インデックスが同じ
        else:
            # 足した価値が0以上なら、両方とる
            if black_value + white_value >= 0:
                score += black_value + white_value
                black_index += 1
                white_index += 1
            # 足した価値が負なら、終わり
            else:
                break

print(score)
