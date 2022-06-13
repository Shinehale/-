def check(ans):
    string = [str(ans), str(ans * 2), str(ans * 3)]
    flag = True
    vis = [False] * 10
    for i in range(3):
        for each in string[i]:
            pos = int(each)
            vis[pos] = True
    for i in range(1, 10):
        if not vis[i]:
            flag = False
    return flag


for hun in range(1, 10):
    for ten in range(1, 10):
        for sev in range(1, 10):
            ans = hun * 100 + ten * 10 + sev
            if ans > 333:
                continue
            if check(ans):
                print(ans,end=" ")
