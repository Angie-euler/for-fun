#include<stdio.h>
int array[]={0,1,2,3,5,8,44};
#define len (sizeof(array)/sizeof(array[0]))
int main()
{
    //int d=-1,x=3;
    char p=1,apple=0;
    apple=sizeof(int) * p;
    printf("%d",apple);
    return 0;
}