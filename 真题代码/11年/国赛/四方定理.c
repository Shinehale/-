# 原题数据有问题，没办法实现评测，但是代码确实是这样改的

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int f(int n, int a[], int idx)
{
    if(n<=0) return 1;
    if(idx==4)  return 0;
    for(int i=(int)sqrt(n); i>=1; i--)
    {
        a[idx] = i;
        if(f(n-i*i,a,idx+1))
            return 1;
    }
    return 0;
}

int main(int argc, char* argv[])
{
    int number;
    printf("输入整数(1~10亿)：");
    scanf("%d",&number);
    int a[] = {0,0,0,0};
    int r = f(number, a, 0);
    printf("%d: %d %d %d %d\n", r, a[0], a[1], a[2], a[3]);
    return 0;
}