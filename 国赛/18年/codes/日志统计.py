R = list(map(int,input().strip().split()))
n, D, K= R[0],R[1],R[2]
a = []
M = 0
for i in range(n):
    R = list(map(int,input().strip().split()))
    ts, id = R[0], R[1]
    M = max(M, id)
    a.append((ts,id))
a.sort(key = lambda x : x[0])
s = [[0] for i in range(M+1)]
for each in a:
    s[each[1]].append(each[0])
for times in range(1,M+1):
    lis = s[times]
    for i in range(1,len(lis)-K+1):
        if lis[i+K-1]<lis[i]+D:
            print(times)
            break
"""
笑死
这不能怨我了吧
纯纯python慢
只有67分
明显数据加强了
思路是对的
"""