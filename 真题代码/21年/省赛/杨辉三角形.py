def calc(a, b):
    res = 1
    for i in range(a):
        res *= b / a
        b -= 1
        a -= 1
    return res


def check(k):
    L, R = 2 * k, Tar
    if R <= L and calc(k, L) != Tar:
        return False
    while L <= R:
        mid = (R - L) // 2 + L
        value = calc(k, mid)
        if value < Tar:
            L = mid + 1
        elif value > Tar:
            R = mid - 1
        else:
            print(int(mid * (mid + 1) // 2) + k + 1)
            return True
    return False



Tar = int(input())
for i in range(16, -1, -1):
    if check(i):
        break
