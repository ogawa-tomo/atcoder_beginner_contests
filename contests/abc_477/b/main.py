class Person:
    def __init__(self, i: int, x: int) -> None:
        self.i = i
        self.x = x

    def __repr__(self) -> str:
        return str(self.i)


N, D = map(int, input().split())
X = list(map(int, input().split()))

people: list[Person] = []
for i in range(N):
    x = X[i]
    person = Person(i + 1, x)
    people.append(person)

people.sort(key=lambda p: p.x)
# print(people)

answers: list[Person] = []
for i in range(N):
    person = people[i]
    ok1 = True
    if i > 0:
        before = people[i - 1]
        ok1 = person.x - before.x >= D
    ok2 = True
    if i < N - 1:
        after = people[i + 1]
        ok2 = after.x - person.x >= D

    if ok1 and ok2:
        answers.append(person)

answers.sort(key=lambda p: p.i)
print(len(answers))
print(*answers)
