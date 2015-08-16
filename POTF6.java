package montecarlo;
import java.util.Random;
/*This is a quick program to figure out how often 3 random points on the perimeter of a circle 
	are on the same half of a circle
	We do this by slicing the circle's circumference into a line/interval from 0 to 1,
	and checking a few extra things to see if a halfcircle that wraps around from 0 to 1
	contains both dots
	The slice is chosen so that the first dot is always at position 0 (and thus also position 1) 
	Program written by Cory H N on or around 08 December 2013.
*/

public class POTF6 {
	public static void main(String[] args){
		double sameHalfCounter = 0; //counts the # of times they're on the same half
		final int ITERATION_COUNT = (int) (Math.pow(2,31)-1);//How many pseudorandom tests we do.  
				//On a i5-3450, 10mil tests takes ~5 sec ; 2^31-1 about 6 minutes.
		double x1; //One point, randomly chosen in the loop
		double x2; //The second point, randomly chosen later
		double highest; //double to save which point has the highest distance from 0 (and thus highest distance from 1)
		double lowest; //double to save which point has the lowest distance from 0.
		for(long n=0; n < ITERATION_COUNT; n++){//run for IT_COUNT times
			x1 = (new Random().nextDouble());//x1 and x2, new randoms
			x2 = (new Random().nextDouble());
			highest = Math.max(x1, x2);//find the highest and lowest
			lowest = Math.min(x1, x2);
			if((highest <=0.5) || ((1 - highest) + lowest <= 0.5) || (lowest >= 0.5)){
				sameHalfCounter++;
			}//if - checks if they're on the same half from 0 to .5, or from .5 to 1, or one that wraps around through the 0/1 conversion
		}//for
		System.out.println("The dots were simulated " + ITERATION_COUNT+ " times." );
		System.out.println("All 3 dots were on the same half " + ((double) sameHalfCounter) / ITERATION_COUNT  + " of the time.");
	}//main
}//class

