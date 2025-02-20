#include<stdio.h>
#include<conio.h>
int main()
{
    int a;
    printf("enter a number");
    scanf("%i",&a);
    if(a%2==0)
    {
        printf("the given number is even");        
    }
    else{
        printf("given number is odd");
    }
}
