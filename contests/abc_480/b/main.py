from collections import defaultdict

N, M = map(int, input().split())


candidates: list[str] = []
votes_by_candidate: defaultdict[str, int] = defaultdict(int)
for _ in range(N):
    s = input()
    candidates.append(s)
# print(candidates)


def matches(name1: str, name2: str):
    if len(name1) != len(name2):
        return False

    false_count = 0
    for i in range(len(name1)):
        n1 = name1[i]
        n2 = name2[i]
        if n1 != n2:
            false_count += 1
        if false_count > 1:
            return False
    return True


def matched_candidate(name: str):
    matched_candidates: list[str] = []
    for candidate in candidates:
        if name == candidate:
            return candidate
        if matches(name, candidate):
            matched_candidates.append(candidate)
    if len(matched_candidates) == 1:
        return matched_candidates[0]
    return None


for _ in range(M):
    t = input()
    candidate = matched_candidate(t)
    if candidate is not None:
        votes_by_candidate[candidate] += 1


for candidate in candidates:
    print(votes_by_candidate[candidate])
