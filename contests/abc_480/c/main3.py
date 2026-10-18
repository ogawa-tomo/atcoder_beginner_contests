class Section:
    def __init__(self, left: int, right: int) -> None:
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return str((self.left, self.right))


N, K, T = map(int, input().split())
A = list(map(int, input().split()))

sections: list[Section] = []
for a in A:
    section = Section(a, a + K)
    sections.append(section)

sections.sort(key=lambda s: s.left)
# print(sections)
new_sections: list[Section] = []
i = 0
while i < N:
    section = sections[i]
    while i < N - 1 and sections[i + 1].left <= section.right:
        section = Section(section.left, sections[i + 1].right)
        i += 1
    new_sections.append(section)
    i += 1

# print(new_sections)


def fill_gap_count(gap: int):
    if gap < 0:
        return 0
    answer = gap // K
    if gap % K != 0:
        answer += 1
    return answer


answer = 0
length = len(new_sections)
for i in range(length):
    section = new_sections[i]
    if i == 0:
        gap = min(T, section.left)
    else:
        prev_section = new_sections[i - 1]
        gap = min(T, section.left) - prev_section.right

    answer += fill_gap_count(gap)

    if i == length - 1:
        gap = T - section.right
        answer += fill_gap_count(gap)

print(answer)
