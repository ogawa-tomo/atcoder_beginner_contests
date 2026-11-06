from fractions import Fraction

T = int(input())

for _ in range(T):
    Px, Py, Qx, Qy, Rx, Ry, Sx, Sy = map(int, input().split())

    dpx = Qx - Px
    dpy = Qy - Py
    drx = Sx - Rx
    dry = Sy - Ry

    mpx = Fraction(Px + Qx, 2)
    mpy = Fraction(Py + Qy, 2)
    mrx = Fraction(Sx + Rx, 2)
    mry = Fraction(Sy + Ry, 2)

    if dpx == 0 and drx == 0:
        if mpy == mry:
            print("Yes")
        else:
            print("No")
    elif dpx == 0 or drx == 0:
        print("Yes")
    else:
        ap = Fraction(dpy, dpx)
        ar = Fraction(dry, drx)
        if ap != ar:
            print("Yes")
        else:
            if dpy == 0:
                if mpx == mrx:
                    print("Yes")
                else:
                    print("No")
            else:
                a = -Fraction(dpx, dpy)
                if mry - mpy == a * (mrx - mpx):
                    print("Yes")
                else:
                    print("No")
