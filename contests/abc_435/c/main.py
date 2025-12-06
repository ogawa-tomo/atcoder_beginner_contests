N = int(input())
A = list(map(int, input().split()))

i = 0
while True:
    # iのドミノが倒れる
    domino_height = A[i]

    # それ以上は倒れないパターン
    if domino_height == 1:
        break

    # 倒れる最後のドミノのインデックス
    fall_domino_last_index = i + domino_height - 1
    if fall_domino_last_index >= N - 1:
        # N-1まで倒れてたら終わり
        i = N - 1
        break

    # 倒れる最後のドミノのインデックスを調べる
    domino_index = fall_domino_last_index
    for j in range(i, fall_domino_last_index + 1):
        # 途中jで倒れたドミノの高さを足したところまで倒れる
        domino_index = max(j + A[j] - 1, domino_index)
    if domino_index >= N - 1:
        i = N - 1
        break
    i = domino_index


print(i + 1)
