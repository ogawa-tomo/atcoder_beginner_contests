# AC
N, Q = map(int, input().split())

# version_num[version]: versionのコンピュータの台数
version_num = [1 for i in range(N)]

min_version = 0

for _ in range(Q):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    if x < min_version:
        print(0)
        continue
    count = 0
    for v in range(min_version, x + 1):
        count += version_num[v]
        version_num[v] = 0
    min_version = x + 1
    # print(version_num)
    # print(version_num)
    version_num[y] += count
    # print(version_num)
    print(count)
