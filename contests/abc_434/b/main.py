N, M = map(int, input().split())


class Bird:
    def __init__(self, kind: int, weight: int):
        self.kind = kind
        self.weight = weight

    def __repr__(self):
        return str((self.kind, self.weight))


birds: list[Bird] = []
for _ in range(N):
    kind, weight = map(int, input().split())
    bird = Bird(kind, weight)
    birds.append(bird)

# print(birds)
for k in range(1, M + 1):
    total_weight = 0
    total_num = 0
    for bird in birds:
        if bird.kind == k:
            total_weight += bird.weight
            total_num += 1
    print(total_weight / total_num)
