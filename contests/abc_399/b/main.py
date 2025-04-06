N = int(input())
P = list(map(int, input().split()))


class Person:
    def __init__(self, number: int, score: int):
        self.number = number
        self.score = score
        self.finalized = False
        self.rank = 0

    def __repr__(self):
        return str(self.score)


def max_score():
    result = 0
    for person in people:
        if person.finalized:
            continue
        result = max(result, person.score)
    return result


# def num_score_x(x):
#     result = 0
#     for person in people:
#         if person.finalized:
#             continue
#         if person.score == x:
#             result += 1
#     return result


people: list[Person] = []
for i, p in enumerate(P):
    people.append(Person(i, p))

# print(people)
# print(max_score())
r = 1
while True:
    score = max_score()
    # print(people)
    # print(score)
    num_finalized = 0
    k = 0
    for person in people:
        if person.finalized:
            num_finalized += 1
            continue
        if person.score == score:
            k += 1
    if num_finalized == N:
        break
    for person in people:
        if person.finalized or person.score != score:
            continue
        person.score = r
        person.finalized = True
    r += k

for person in people:
    print(person.score)
