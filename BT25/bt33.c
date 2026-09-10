#include <stdio.h>
#include <math.h>

int main(void){
	double e= 2.718281; //defining e 

	printf("Enter x:\n");
	float x;
	scanf("%f", &x);

	for(int i=0;i<5000;i++){
		double fx= pow(e,x) - 2;
		double f_x= pow(e,x);
		double y= x- (fx/f_x); //using difference eqn to get new iteration
		x=y;
	}
	double fx= pow(e,x) -2; //defining final value 
	printf("The root of the eqn is: %.4f\n",x);
	printf("The value of the eqn at %.4f is %.4f\n",x,fx);
}
