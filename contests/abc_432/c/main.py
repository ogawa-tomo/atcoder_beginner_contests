import sys

N, X, Y = map(int, input().split())
A = list(map(int, input().split()))

mod: int | None = None
N_min = 0
N_max = sys.maxsize
for a in A:
    # 飴の配り方により、Xa以上Ya以下の重量を実現できる
    # ただし、XaやYaとY-Xを法として合同な数のみ
    if mod is None:
        # modが未設定であれば設定
        mod = (X * a) % (Y - X)
    else:
        # modが設定済みであれば、modがズレていたらその時点で不可能
        if (X * a) % (Y - X) != mod:
            print(-1)
            exit()
    N_min = max(N_min, X * a)
    N_max = min(N_max, Y * a)
    if N_min > N_max:
        print(-1)
        exit()
# print(N_min, N_max)
answer = 0
for a in A:
    # X * (a - y) + Y * y = N_max
    # N_maxを実現するときのy
    y = (N_max - a * X) / (Y - X)

    # modが一致することは確認済みなのでyは絶対に整数
    # if not y.is_integer():
    #     print(-1)
    #     exit()
    answer += int(y)

print(answer)
