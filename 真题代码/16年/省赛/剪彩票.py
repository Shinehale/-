import itertools


def find(x):
    if x==fa[x]:return x
    else:
        fa[x]=find(fa[x])
        return fa[x]


def judge(x, y):
    if x > y:
        x, y = y, x
    if x // 4 == y // 4 and y == x + 1:
        return True
    if x // 4 + 1 == y // 4 and y == x + 4:
        return True
    return False


def check(Lis):
    global fa
    fa = [i for i in range(12)]
    for i in range(1, 5):
        for k in range(i):
            # print(Lis[i],Lis[k],judge(Lis[i],Lis[k]),end="  ")
            if judge(Lis[i], Lis[k]):
                fa[find(Lis[i])] = find(Lis[k])
    flag = True
    for i in range(12):
        fa[i]=find(i)
    for i in range(4):
        if fa[Lis[i]] != fa[Lis[i + 1]]:
            flag = False
    return flag


tot = 0
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
fa = [i for i in range(12)]
newList = list(itertools.combinations(a, 5))
for each in newList:
    if check(each):
        tot += 1
print(tot)
