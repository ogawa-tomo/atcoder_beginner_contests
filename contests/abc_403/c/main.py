N, M, Q = map(int, input().split())


class Person:
    def __init__(self) -> None:
        self.all = False
        self.view: set[int] = set()
        # self.view = [False] * M # このやり方だと通らない…なぜ？リストが長すぎるから？

    def can_view(self, page_num):
        if self.all:
            return True
        return page_num in self.view
        # return self.view[page_num]

    def allow_all(self):
        self.all = True

    def allow_page(self, page_num):
        self.view.add(page_num)
        # self.view[page_num] = True


people = [Person() for _ in range(N)]

for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        x, y = map(int, query[1:])
        x -= 1
        y -= 1
        person = people[x]
        person.allow_page(y)
    elif query[0] == 2:
        x = query[1]
        x -= 1
        person = people[x]
        person.allow_all()
    elif query[0] == 3:
        x, y = map(int, query[1:])
        x -= 1
        y -= 1
        person = people[x]
        if person.can_view(y):
            print("Yes")
        else:
            print("No")
