#include<stdio.h>
#include<math.h>
float f(float x);
int main()
{
    float x =5.0/8;
    if(f(x)==4) printf("Correct Answer\n");
    else printf("Wrong Anser\n");
    return 0;
}
float f(float x)
{
    return (2*x+sqrt(4*x*x-1))/(2*x-sqrt(4*x*x-1));
}