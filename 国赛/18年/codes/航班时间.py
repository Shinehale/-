import datetime

n = int(input())
ans = []
li = []
for i in range(n * 2):
    s = list(input().split())
    if len(s) > 2:
        if s[2][2] == '1':
            dt1 = datetime.datetime.strptime('10 ' + s[0], '%d %H:%M:%S')
            dt2 = datetime.datetime.strptime('11 ' + s[1], '%d %H:%M:%S')
        elif s[2][2] == '2':
            dt1 = datetime.datetime.strptime('10 ' + s[0], '%d %H:%M:%S')
            dt2 = datetime.datetime.strptime('12 ' + s[1], '%d %H:%M:%S')
    else:
        dt1 = datetime.datetime.strptime(s[0], '%H:%M:%S')
        dt2 = datetime.datetime.strptime(s[1], '%H:%M:%S')
    td1 = dt2 - dt1
    li.append((td1.seconds + (td1.days) * 24 * 3600))
i = 0
while i < len(li):
    an = (li[i] + li[i + 1]) // 2
    i += 2
    ans.append(an)
for j in range(n):
    h = ans[j] // 3600
    m = (ans[j] % 3600) // 60
    s = ans[j] - h * 3600 - m * 60
    print('{:02d}:{:02d}:{:02d}'.format(int(h), int(m), int(s)))
