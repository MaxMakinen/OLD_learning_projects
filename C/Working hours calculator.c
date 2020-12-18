#include <stdio.h>


int main(void) {

    float hours[30];	
    float time = 0.0, total = 0.0, average = 0.0;
    int days, i;
	
    printf("The program adds up the total working hours done over a number\nof days that you specify, as well as the average length of a working day.\n\n");
    printf("How many days?:");
    scanf("%d", &days);
	
    for(i = 0; i < days; i++) {
         printf("Anna %d. päivän työtunnit:", i+1);
         scanf("%f", &hours[i]);
         }
	 
    for (i = 0; i < days; i++) {
        total = total + hours[i];
        }

    average = total / days;
		
	
    printf("\nTotal working hours: %.1f\n", total);
    printf("Length of average day: %.1f\n", average);
	
    for (i = 0; i < days; i++) {
        if(i == 0){
        printf("Syötetyt tunnit: %.1f ", hours[i]);
        }
        else {
            printf("%.1f ", hours[i]);
            }}
		
    return 0;
}