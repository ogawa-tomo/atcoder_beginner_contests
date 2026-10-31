from collections import defaultdict

N = int(input())

votes_by_name: defaultdict[str, int] = defaultdict(int)
for _ in range(N):
    s = input().upper()
    votes_by_name[s] += 1

# print(votes_by_name)
votes = list(votes_by_name.values())
print(max(votes))
