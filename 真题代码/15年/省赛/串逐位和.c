#include <stdio.h>
#include <string.h>
int f(const char s[], int begin, int end)
{
    int mid;
    if(end-begin==1) return s[begin] - '0';
    mid = (begin+end)/2;
    return f(s,begin,mid)+f(s,mid,end);
}
int main()
{
    char s[] = "82791276526645328666454364634222489763382233";
    printf("%d\n",f(s,0,strlen(s)));
    return 0;
}