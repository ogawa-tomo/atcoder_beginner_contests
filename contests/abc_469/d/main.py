class Finalist:
    def __init__(self, a: int, b: int) -> None:
        self.a = min(a, b)
        self.b = max(a, b)

    def includes(self, x: int):
        return self.a == x or self.b == x

    def get_set(self):
        return {self.a, self.b}

    def __eq__(self, other) -> bool:
        if not isinstance(other, Finalist):
            raise
        return self.a == other.a and self.b == other.b

    def __hash__(self) -> int:
        return hash((self.a, self.b))

    def __repr__(self) -> str:
        return str((self.a, self.b))


N, M = map(int, input().split())

finalists: list[Finalist] = []
for _ in range(M):
    a, b = map(int, input().split())
    finalist = Finalist(a, b)
    finalists.append(finalist)


# この時点で、答えは(candid_a, x)と(candid_b, x)に絞られる
candid_a = finalists[0].a
candid_b = finalists[0].b

all_includs_candid_a = True
all_includs_candid_b = True
for i in range(1, M):
    finalist = finalists[i]
    if not finalist.includes(candid_a):
        all_includs_candid_a = False
    if not finalist.includes(candid_b):
        all_includs_candid_b = False

if all_includs_candid_a and all_includs_candid_b:
    # (candid_a, x)と(candid_b, x)
    answer = N - 1 + N - 2
    print(answer)
    exit()
elif all_includs_candid_a or all_includs_candid_b:
    answer = N - 1
    print(answer)
    exit()

# candid_aが決勝進出していないときも、常に決勝進出しているやつの集合
candid_a_other_candid: set[int] = set()
candid_b_other_candid: set[int] = set()
candid_a_not_finalist_emerged = False
candid_b_not_finalist_emerged = False
for i in range(1, M):
    finalist = finalists[i]
    if not finalist.includes(candid_a):
        if not candid_a_not_finalist_emerged:
            candid_a_other_candid = finalist.get_set()
            candid_a_not_finalist_emerged = True
        else:
            candid_a_other_candid &= finalist.get_set()
    if not finalist.includes(candid_b):
        if not candid_b_not_finalist_emerged:
            candid_b_other_candid = finalist.get_set()
            candid_b_not_finalist_emerged = True
        else:
            candid_b_other_candid &= finalist.get_set()

# print(candid_a_other_candid)
# print(candid_b_other_candid)
answers: set[Finalist] = set()
for candid in candid_a_other_candid:
    answers.add(Finalist(candid_a, candid))
for candid in candid_b_other_candid:
    answers.add(Finalist(candid_b, candid))
# print(answers)
print(len(answers))
