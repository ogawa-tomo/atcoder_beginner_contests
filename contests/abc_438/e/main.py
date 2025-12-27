# ためしに書いただけ


class Bucket:
    def __init__(self, i: int, person: int, water: int):
        self.i = i
        self.person = person
        self.water = water

    def __repr__(self):
        return str((self.i, self.person, self.water))


N, Q = map(int, input().split())

buckets = [Bucket(i, i, 0) for i in range(N + 1)]
print(buckets)

A = [0, *list(map(int, input().split()))]
for i in range(1, 11):
    print(f"{i}回目の操作")
    for bucket in buckets:
        bucket.water += bucket.person
    for bucket in buckets:
        bucket.person = A[bucket.person]
    print(buckets)


# print(buckets)
for _ in range(Q):
    t, b = map(int, input().split())
