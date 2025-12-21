# MLE
N = int(input())


class A:
    def __init__(self, i: int, a_list: list[int]):
        self.i = i
        self.a_list = a_list
        self.length = len(self.a_list)

    # このソートの負荷が高い
    def __lt__(self, other):
        length = min(self.length, other.length)
        for k in range(length):
            if self.a_list[k] == other.a_list[k]:
                continue
            return self.a_list[k] < other.a_list[k]
        return self.length < other.length


A_list: list[A] = [A(0, [])]
for i in range(1, N + 1):
    x, y = map(int, input().split())
    a = A_list[x]
    a_list = a.a_list[:]
    a_list.append(y)
    append_A = A(i, a_list)
    A_list.append(append_A)

A_list = A_list[1:]
A_list.sort()
print(" ".join([str(a.i) for a in A_list]))
