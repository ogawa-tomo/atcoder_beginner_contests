# TLE
import sys

sys.setrecursionlimit(12000000)

S = list(map(int, input()))


class Calc:
    def __init__(self):
        self.answer = 0

    def calc(self, s: list[int]):
        if len(s) == 1:
            print(self.answer + s[0] + 1)
            exit()
        if s[-1] == 0:
            self.answer += 1
            self.calc(s[:-1])
        num = s[-1]
        self.answer += num

        # ここで桁数分のループを回すから
        for i in range(len(s)):
            s[i] = (s[i] - num) % 10
        self.calc(s)


Calc().calc(S)
