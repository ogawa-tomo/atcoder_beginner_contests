N = int(input())
A = list(map(int, input().split()))


class Num:
    def __init__(self, i: int, value: int):
        self.i = i
        self.value = value

    def __repr__(self):
        return str((self.i, self.value))

    def __lt__(self, other):
        return self.i < other.i


# num_dict[n]: 値がnであるようなインデックスのリスト

nums: list[Num] = []
for i in range(N):
    a = A[i]
    num = Num(i, a)
    nums.append(num)

nums.sort()
print(nums)

# A.sort()
# print(A)
