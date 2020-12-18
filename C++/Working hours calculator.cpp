#include <iostream>
using namespace std;

void print_array(int, float[]);

int main()
{
    float elements[30], total, average = 0;
    int days, i;
	
    cout << "The program calculates the total amount of\nwork hours during a given time frame and the average work day length.\nHow many days:" << endl;
    cin >> days; // Asks for the amount of days worked.
    for(i = 0 ; i < days ; i++){ // Uses a for loop with days worked to inquire about the working hours of each day.
        cout << "Input hours of workday " << i+1 <<": ";
        cin >> elements[i];
        total += elements[i];
    }
    average = total / days;
    cout << "Total work hours: " << total << endl; // Outputs the total hours worked.
    cout << "Average workday length: " << average << endl; // Outputs the length of the average workday.
    for(i = 0 ; i < days ; i++) // Outputs all the inputted hours for review.
        if (i == 0)
            cout << "Inputted hours: " << elements[i];
        else
            cout << " " << elements[i];
    cout << " " << endl;
}