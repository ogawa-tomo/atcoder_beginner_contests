N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))


class DFS:
    def __init__(self) -> None:
        self.answer = 0

    def dfs(self, current_list: list[int], usable_nums: set[int]):
        if len(current_list) == N:
            if P < current_list and current_list < Q:
                self.answer += 1

        for num in usable_nums:
            new_usable_nums = usable_nums.copy()
            new_usable_nums.remove(num)
            new_list = current_list.copy()
            new_list.append(num)
            self.dfs(new_list, new_usable_nums)


dfs = DFS()
dfs.dfs([], set(range(1, N + 1)))
print(dfs.answer)
