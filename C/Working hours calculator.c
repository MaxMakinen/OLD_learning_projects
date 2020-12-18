#include <stdio.h>


int main(void) {

    float hours[30];	
    float time = 0.0, total = 0.0, average = 0.0;
    int days, i;
	
    printf("The program adds up the total working hours done over a number\nof days that you specify, as well as the average length of a working day.\n\n");

/*Asks for the amount of day to input and then applies that to a for loop asking for the hours in each day*/
    printf("How many days?:");
    scanf("%d", &days);	
    for(i = 0; i < days; i++) {
         printf("Give the hours of day %d:", i+1);
         scanf("%f", &hours[i]);
         }

/*Calculates the total worked*/	 
    for (i = 0; i < days; i++) {
        total = total + hours[i];
        }

    average = total / days;
		

/*Outputs the total hours worked as well as the average days lenght. Afterwards outputs all the given working hours for review*/	
    printf("\nTotal working hours: %.1f\n", total);
    printf("Length of average day: %.1f\n", average);
	
    for (i = 0; i < days; i++) {
        if(i == 0){
        printf("Input hours: %.1f ", hours[i]);
        }
        else {
            printf("%.1f ", hours[i]);
            }}
		
    return 0;
}