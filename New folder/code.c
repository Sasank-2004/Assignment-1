#include<stdio.h>
#include<math.h>
// This functions evaluates the LHS of Equation given in the Question for any arbitary x 
float f(float x)
{
    return (2*x+sqrt(4*x*x-1))/(2*x-sqrt(4*x*x-1));
}
int main ()
{
    float x=5.0/8;
    if(f(x)==4.0) printf("Correct Answer\n"); // we check if x=5/8 is the solution of f(x)=4  and print "correct answer " if the answer we obtained by solving manually is correct 
    else printf("Wrong Answer");              // we print "Wrong answer" if the answer we obtained by solving the problem manually is incorrect 
}
