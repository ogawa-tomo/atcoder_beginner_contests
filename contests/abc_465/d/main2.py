# AC
T = int(input())


def get_ancestors(x: int, k: int):
    x_ = x
    ancesters: list[int] = [x_]
    while x_ > 0:
        x_ //= k
        ancesters.append(x_)
    ancesters.reverse()
    return ancesters


for _ in range(T):
    X, Y, K = map(int, input().split())
    x_ancestors = get_ancestors(X, K)
    y_ancestors = get_ancestors(Y, K)
    # print(x_ancestors, y_ancestors)

    distance = 0

    while x_ancestors and y_ancestors and x_ancestors[-1] != y_ancestors[-1]:
        if len(x_ancestors) > len(y_ancestors):
            x_ancestors.pop()
            distance += 1
        elif len(y_ancestors) > len(x_ancestors):
            y_ancestors.pop()
            distance += 1
        else:
            x_ancestors.pop()
            y_ancestors.pop()
            distance += 2

    print(distance)
