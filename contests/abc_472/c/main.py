class Oyatsu:
    def __init__(self, calorie: int) -> None:
        self.calorie = calorie
        self.eaten = False


N, M, K = map(int, input().split())
A = list(map(int, input().split()))

oyatsu_list: list[Oyatsu] = []
for a in A:
    oyatsu_list.append(Oyatsu(a))

calorie = 0
for i in range(N):
    if i >= M and oyatsu_list[i - M].eaten:
        calorie -= oyatsu_list[i - M].calorie
    oyatsu = oyatsu_list[i]
    if calorie + oyatsu.calorie <= K:
        print("Yes")
        calorie += oyatsu.calorie
        oyatsu.eaten = True
    else:
        print("No")
