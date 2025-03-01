class String:
    def __init__(self, string: str):
        self.string = string
        self.length = len(string)

    def __lt__(self, other):
        return self.length < other.length

    def __repr__(self):
        return self.string


N = int(input())
S: list[String] = []


for _ in range(N):
    s = String(input())
    S.append(s)
S.sort()
print("".join([s.string for s in S]))
