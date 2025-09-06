N, Q = map(int, input().split())
A = list(map(int, input().split()))
sections = 0

# spaces[i]: i番目のマス。Falseなら白、Trueなら黒
spaces = [False] * N

# N = 1のケースに注意！

for a in A:
    i = a - 1
    if N == 1:
        # 黒を白に
        if spaces[i]:
            sections = 0
        # 白を黒に
        else:
            sections = 1
    else:
        # 黒を白にする場合
        if spaces[i]:
            # 左端
            if i == 0:
                pass
                # 右隣が黒なら、変わらない
                if spaces[i + 1]:
                    pass
                # 右隣が白なら、-1
                else:
                    sections -= 1
            # 右端
            elif i == N - 1:
                # 左隣が黒なら、変わらない
                if spaces[i - 1]:
                    pass
                # 左隣が白なら、-1
                else:
                    sections -= 1
            # 真ん中
            else:
                # 両隣が黒なら、+1
                if spaces[i - 1] and spaces[i + 1]:
                    sections += 1
                # 両隣が白なら、-1
                elif not spaces[i - 1] and not spaces[i + 1]:
                    sections -= 1
                # 片方が黒、片方が白なら、変わらない
        # 白を黒にする場合
        else:
            # 左端
            if i == 0:
                # 右隣が黒なら、変わらない
                if spaces[i + 1]:
                    pass
                # 右隣が白なら、+1
                else:
                    sections += 1
            # 右端
            elif i == N - 1:
                # 左隣が黒なら、変わらない
                if spaces[i - 1]:
                    pass
                # 左隣が白なら、+1
                else:
                    sections += 1
            # 真ん中
            else:
                # 両隣が黒なら、-1
                if spaces[i - 1] and spaces[i + 1]:
                    sections -= 1
                # 両隣が白なら、+1
                elif not spaces[i - 1] and not spaces[i + 1]:
                    sections += 1
                # 片方が黒、片方が白なら、変わらない
    spaces[i] = not spaces[i]
    # answers.append(sections)
    print(sections)
