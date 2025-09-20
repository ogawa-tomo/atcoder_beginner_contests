import sys

sys.setrecursionlimit(10**9)

N = int(input())


class Skill:
    def __init__(self) -> None:
        self.connected: list[Skill] = []
        self.acquired = False


skills: list[Skill] = []
for _ in range(N):
    skills.append(Skill())

acquired_skills: list[Skill] = []
for i in range(N):
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        skills[i].acquired = True
        acquired_skills.append(skills[i])
        continue
    a -= 1
    b -= 1
    skills[a].connected.append(skills[i])
    skills[b].connected.append(skills[i])


def dfs(skill: Skill):
    skill.acquired = True
    for neighbor in skill.connected:
        if not neighbor.acquired:
            dfs(neighbor)


for acquired_skill in acquired_skills:
    dfs(acquired_skill)

answer = 0
for skill in skills:
    if skill.acquired:
        answer += 1
print(answer)
