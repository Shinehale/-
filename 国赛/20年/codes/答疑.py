n = int(input())
timelist = []
sumlist = []
ci = 0
res = 0
for i in range(n):
    each = [int(i) for i in input().split()]
    timelist.append(each)
for i in range(n):
    ci += timelist[i][2]
for i in range(n):
    sum = 0
    for j in timelist[i]:
        sum += j
    sumlist.append(sum)
sumlist.sort()
for i in sumlist:
    res += n * i
    n -= 1
print(res - ci)
