def calc(x,y):
    ans=(y-x+1)*(y+x)//2
    return ans
for i in range(1,100):
    for j in range(1,i):
        # print(calc(j,i))
        if calc(j,i)==236:
            print(j)