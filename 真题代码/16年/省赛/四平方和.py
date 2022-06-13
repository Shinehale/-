import math

n = int(input())
sqn = int(math.sqrt(n))


def f(n):
    for a in range(sqn):
        bm = int(math.sqrt(n - a * a)) + 1
        for b in range(a, bm):
            cm = int(math.sqrt(n - a * a - b * b)) + 1
            for c in range(b, cm):
                t = n - a * a - b * b - c * c
                d = int(math.sqrt(t))
                if d * d == t and d >= c:
                    print(a, b, c, d, sep=' ')
                    return


f(n)
