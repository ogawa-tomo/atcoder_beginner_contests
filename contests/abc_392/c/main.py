from typing import Union

N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))


class Zekken:
    def __init__(self, num) -> None:
        self.num = num
        self.person: Union[Person, None] = None


class Person:
    def __init__(self) -> None:
        self.zekken: Union[Zekken, None] = None
        self.looking: Union[Person, None] = None


people = [Person() for _ in range(N + 1)]
zekkens = [Zekken(num) for num in range(N + 1)]

for i in range(1, N + 1):
    p = P[i - 1]
    q = Q[i - 1]
    person = people[i]
    zekken = zekkens[q]
    person.zekken = zekken
    zekken.person = person
    looking_to_person = people[p]
    person.looking = looking_to_person

answers = []
for i in range(1, N + 1):
    person1: Union[Person, None] = zekkens[i].person
    if (
        person1 is not None
        and person1.looking is not None
        and person1.looking.zekken is not None
    ):
        answers.append(str(person1.looking.zekken.num))

print(" ".join(answers))
