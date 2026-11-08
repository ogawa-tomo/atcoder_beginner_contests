from typing import Callable


N = int(input())


def question(left: int, right: int):
    print("?", left, right, flush=True)
    return input() == "Yes"


def shakutori(
    min_i: int,
    max_i: int,
    condition: Callable[[int, int], bool],
    process: Callable[[int, int], None],
):
    right = min_i
    for left in range(min_i, max_i + 1):
        if right < left:
            right = left

        while right + 1 <= max_i and condition(left, right + 1):
            right += 1

        process(left, right)


class Process:
    def __init__(self) -> None:
        self.answer = 0

    def process(self, left: int, right: int):
        self.answer += right - left


p = Process()
shakutori(1, N, question, p.process)

print("!", p.answer, flush=True)
exit()
