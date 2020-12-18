#include <iostream>
#include <string>
using namespace std;
class Dog {
    public:
    int age;
    string name, breed, voice;
	
   // constructor
    Dog();
    Dog(int new_age, string new_name, string new_breed, string new_voice);
    void PrintInformation();
    string Bark();
};

Dog::Dog()
{
    name = "Nameless";
    age = 0;
    breed = "breedless";
    voice = "Bork";
}
Dog::Dog(int new_age, string new_name, string new_breed, string new_voice)
{
    age   = new_age;
    name  = new_name;
    breed = new_breed;
    voice = new_voice;
}
   // method PrintInformation()
void Dog::PrintInformation()
{
    cout << "Name: " << name << endl << "Age: " << age << endl << "Race: " << breed << endl;
}
   // method Bark()
string Dog::Bark()
{
    return voice;
}
int main()
{
    Dog buffy(2, "Buffy", "Bulldog", "Hau!!!");
    buffy.PrintInformation();
    cout << "Dog says: " << buffy.Bark();
}