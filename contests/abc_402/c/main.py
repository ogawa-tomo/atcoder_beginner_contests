N, M = map(int, input().split())


class Ingredient:
    def __init__(self) -> None:
        self.dishes: list[Dish] = []


class Dish:
    def __init__(self) -> None:
        self.ingredients: list[Ingredient] = []
        self.nigate_num = 0


ingredients = [Ingredient() for _ in range(N)]
dishes = [Dish() for _ in range(M)]
for i in range(M):
    query = list(map(int, input().split()))
    K = query[0]
    A = query[1:]
    dish = dishes[i]
    for a in A:
        ingredient = ingredients[a - 1]
        ingredient.dishes.append(dish)
    dish.nigate_num = len(A)

answer = 0
B = list(map(int, input().split()))
for b in B:
    ingredient = ingredients[b - 1]
    for dish in ingredient.dishes:
        dish.nigate_num -= 1
        if dish.nigate_num == 0:
            answer += 1
    print(answer)
