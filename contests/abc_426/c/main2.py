# TLE
N, Q = map(int, input().split())

computers = [i for i in range(N)]

# 現在の最低バージョン
min_version = 0
# version_num[version]: version以下のコンピュータの台数
version_num = [i + 1 for i in range(N)]

# print(version_num)


# # version以下のコンピュータの台数
# def under_version_num(version):
#     if version < min_version:
#         return 0
#     return version_num[version]


for _ in range(Q):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    if x < min_version:
        print(0)
        continue
    count = version_num[x]
    for v in range(min_version, x + 1):
        version_num[v] = 0
    # print(version_num)
    min_version = max(x + 1, min_version)
    for v in range(min_version, y):
        version_num[v] -= count
    # print(version_num)
    print(count)
