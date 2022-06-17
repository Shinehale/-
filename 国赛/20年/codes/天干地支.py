n = int(input())
a = ['jia', 'yi', 'bing', 'ding', 'wu', 'ji', 'geng', 'xin', 'ren', 'gui']
b = ['zi', 'chou', 'yin', 'mao', 'chen', 'si', 'wu', 'wei', 'shen', 'you', 'xu', 'hai']
d = n - 4
a1 = d % 10
b1 = d % 12
print(a[a1] + b[b1])
