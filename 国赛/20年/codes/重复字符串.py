import collections

k = int(input())
s = input()
l = len(s)

if l % k:
    print(-1)
else:
    ans = 0
    for i in range(0, l // k):
        lis = [s[j] for j in range(i, l, l // k)]
        d = dict(collections.Counter(lis))
        ans += (k - max(d.values()))
    print(ans)
