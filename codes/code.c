#include<stdio.h>
#include<math.h>
float f(float x);
int main()
{
    float x =5.0/8;
    if(f(x)==4) printf("Correct Answer\n");
    else printf("Wrong Anser\n");
    float i=0.5;
    FILE *fp;
    fp = fopen("output.txt","w");
    fprintf(fp,"x\t\ty\n");
    for(i=0.5;i<4;i=i+0.01) fprintf(fp,"%f\t\t%f\n",i,f(i));
    fclose(fp);
    return 0;
}
float f(float x)
{
    return (2*x+sqrt(4*x*x-1))/(2*x-sqrt(4*x*x-1));
}
