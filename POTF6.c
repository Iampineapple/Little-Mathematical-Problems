/*This is a quick program to figure out how often 3 random points on the perimeter of a circle 
	are on the same half of a circle
	We do this by slicing the circle's circumference into a line/interval from 0 to 1,
	and checking a few extra things to see if a halfcircle that wraps around from 0 to 1
	contains both dots
	The slice is chosen so that the first dot is always at position 0 (and thus also position 1) 
	Program written by Cory H N on or around 08 December 2013.
	Translated from Java to C on or around 9 Jan 2014.
*/

#include <stdio.h> //for things
#include <stdlib.h> //for random
#include <time.h> //for time to use as a random seed
#include <math.h>

double max(double x1, double x2);
double min(double x1, double x2);

int main(){
	double sameHalfCounter = 0; //counter of how many times they're all on the same half
	long iterationCount = (long) (pow(2,31) - 1);//Number of randomizations to perform
	double x1; //Dot two
	double x2; //Dot three
	double highest;
	double lowest;
	long n; //iterator
	
	
	//For iterationCount iterations, randomize the location of x1 and x2, 
	//then do some math to check if they are all on the same half of the circle
	for(n=0 ; n < iterationCount; n++){
		x1 = ((double)rand()/(double)RAND_MAX);
		x2 = ((double)rand()/(double)RAND_MAX);
		highest = max(x1, x2);
		lowest = min(x1, x2);
		if((highest <=0.5) || ((1 - highest) + lowest <= 0.5) || (lowest >= 0.5)){
				sameHalfCounter++;
		}//if 
	}//for
	
	printf("The dots were simulated %ld times.\n", iterationCount);
	printf("All 3 dots were on the same half %f times, or %f of the time", sameHalfCounter, ((sameHalfCounter) / iterationCount));

	return 0;
}//main

double max(double x1, double x2){
	return ((x1 > x2)?x1:x2);
}//max

double min(double x1, double x2){
	return ((x1 < x2)?x1:x2);
}//min