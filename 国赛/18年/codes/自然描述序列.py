# R = list(map(int,input().split()))
# n = R[0]
# a = [ 0,1,2]
# for i in range( 2, n ):
#     for j in range(a[i]):
#         a.append(i)
# print(a)
g = [0, 1, 2]
N = 100010
for i in range(N):
    g.append(0)

j = 2
for i in range(2, N):
    for k in range(g[i]):
        if j >= N:
            break
        g[j] = i
        j += 1
R = list(map(int, input().split()))
n = R[0]
i = 0
s, t = 0, 0
while True:
    i = i + 1
    s += i * g[i]
    if s >= n:
        s -= i * g[i]
        print(t + int((n - s + i - 1) / i))
        break
