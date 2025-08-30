# WA
rt, ct, ra, ca = map(int, input().split())
N, M, L = map(int, input().split())


class Query:
    def __init__(self, direction: str, distance: int):
        self.direction = direction
        self.distance = distance

    def __repr__(self):
        return f"[{self.direction}, {self.distance}]"


class Person:
    def __init__(self, r: int, c: int):
        self.r = r
        self.c = c

    # def move(self, query: Query):
    #     if query.direction == "U":
    #         self.r -= query.distance
    #     elif query.direction == "D":
    #         self.r += query.distance
    #     elif query.direction == "R":
    #         self.c += query.distance
    #     elif query.direction == "L":
    #         self.c -= query.distance
    def move(self, direction: str, distance: int):
        if direction == "U":
            self.r -= distance
        elif direction == "D":
            self.r += distance
        elif direction == "R":
            self.c += distance
        elif direction == "L":
            self.c -= distance


takahashi = Person(rt, ct)
aoki = Person(ra, ca)

S: list[Query] = []
T: list[Query] = []

for _ in range(M):
    sa = input().split()
    S.append(Query(sa[0], int(sa[1])))
for _ in range(L):
    tb = input().split()
    T.append(Query(tb[0], int(tb[1])))

# print(S)
# print(T)
# print(S[M - 1])
answer = 0
si = 0
ti = 0
if takahashi.c == aoki.c and takahashi.r == aoki.r:
    answer += 1
while True:
    is_same = takahashi.c == aoki.c and takahashi.r == aoki.r
    before_takahashi_c = takahashi.c
    before_takahashi_r = takahashi.r
    before_aoki_c = aoki.c
    before_aoki_r = aoki.r
    # print(takahashi.c, takahashi.r, aoki.c, aoki.r)

    if si >= M and ti >= L:
        break
    if si < M and ti >= L:
        s = S[si]
        takahashi.move(s.direction, s.distance)
        si += 1
        if (
            before_takahashi_c < aoki.c
            and aoki.c < takahashi.c
            and aoki.r == takahashi.r
        ):
            answer += 1
        if (
            before_takahashi_r < aoki.r
            and aoki.r < takahashi.r
            and aoki.c == takahashi.c
        ):
            answer += 1
    if si >= M and ti < L:
        t = T[ti]
        aoki.move(t.direction, t.distance)
        ti += 1
        if (
            before_aoki_c < takahashi.c
            and takahashi.c < aoki.c
            and aoki.r == takahashi.r
        ):
            answer += 1
        if (
            before_aoki_r < takahashi.r
            and takahashi.r < aoki.r
            and aoki.c == takahashi.c
        ):
            answer += 1
    if si < M and ti < L:
        s = S[si]
        t = T[ti]

        # 同じ方向に行く
        if is_same and s.direction == t.direction:
            # print("hoge")
            # print(s.distance, t.distance)
            answer += min(s.distance, t.distance) - 1
        if s.distance < t.distance:
            takahashi.move(s.direction, s.distance)
            aoki.move(t.direction, s.distance)
            si += 1
            t.distance -= s.distance
        elif t.distance < s.distance:
            takahashi.move(s.direction, t.distance)
            aoki.move(t.direction, t.distance)
            ti += 1
            s.distance -= t.distance
        else:
            takahashi.move(s.direction, s.distance)
            aoki.move(t.direction, t.distance)
            si += 1
            ti += 1
        # クロス
        # if s

    # クロスした場合
    # if (s.direction == "U" or s.direction == "D") and (
    #     t.direction == "R" or t.direction == "L"
    # ):
    #     if min(before_takahashi_r, takahashi.r) < aoki.r and aoki.r < max(
    #         before_takahashi_r, takahashi.r
    #     ):
    #         answer += 1
    # if (s.direction == "R" or s.direction == "L") and (
    #     t.direction == "U" or t.direction == "D"
    # ):
    #     if min(before_aoki_r, aoki.r) < takahashi.r and takahashi.r < max(
    #         before_aoki_r, aoki.r
    #     ):
    #         answer += 1
    # if

    # 一致した場合
    if takahashi.r == aoki.r and takahashi.c == aoki.c:
        answer += 1

print(answer)
