/*
This is a simple school project where the task was to make a phonebook file that checks if the input information exists in the file, 
if they're there they get deleted. Otherwise it outputs that "The person that you're loking for was not in the file".
*/


#include <stdio.h>
#include <string.h>

int compare (char a[20], char b[20], char c[20], char d[20]);

int
main (void)
{
  int i, val, to_remove = 10, compare, last_compare;
  FILE *phonebook;
  char list[] = "luettelo.txt";
  char amount[3], remove_first_name[20], remove_last_name[20];


  struct person
  {
    char first_name[20];
    char last_name[20];
    char phonenumber[20];
  };
  struct person person_list[4];

/* Asks for the first and last name that are to be removed */
  printf ("First name:");
  scanf ("%s", remove_first_name);
  printf ("Last name:");
  scanf ("%s", remove_last_name);

/* Attempts to open the file, followed by the check of whether or not the given names can be found */
  if ((phonebook = fopen (list, "r")) == NULL)
    {
      printf ("File not found!");
      return 0;
    }
  else
    {
        
/*For this excercise that this was coded for we knew that the given lists are no longer than 4*/
      for (i = 0; i < 4; i++)
	{
	    
/*We knew that the first line on the list gave us the exact amount of lines in the file, so we atoi that into the integer val*/
	  if (i == 0)
	    {
	      fscanf (phonebook, "%s%s%s%s", amount,
		      person_list[i].first_name, person_list[i].last_name,
		      person_list[i].phonenumber);
	      val = atoi (amount);
	    }
	    
/*we copy the information from the file into a the person_list structure*/
	  else
	    {
	      fscanf (phonebook, "%s%s%s", person_list[i].first_name,
		      person_list[i].last_name, person_list[i].phonenumber);
	    }
	}
    }

/*Here we do comparisons to see if the names that were given as input can be found in the file*/
  for (i = 0; i < 4; i++)
    {
      compare = strcmp (remove_first_name, person_list[i].first_name);
      last_compare = strcmp (remove_last_name, person_list[i].last_name);
      if (compare == 0)
	{
	  if (last_compare == 0)
	    {
	      to_remove = i;
	    }
	  else
	    {
	      continue;
	    }
	}
      else
	{
	  continue;
	}
    }
    
/*if to_remove hasn't been changed from it's original value, the names were not found*/
  if (to_remove == 10)
    {
      printf ("the person that you're looking for was not in the file.");
      return 0;
    }
  else
    {
      for (i = 0; i < 4; i++)
	{
	  if (i == to_remove)
	    {
	      continue;
	    }
	  else if (i == 0)
	    {
	        
/*As we re-write the file we return the new length of the list(val) to be the first thing on the file*/
	      val = --val;
	      fprintf (phonebook, "%d%s%s%s", val, person_list[i].first_name,
		       person_list[i].last_name, person_list[i].phonenumber);
	    }
	  else
	    {
	      fprintf (phonebook, "%s%s%s", person_list[i].first_name,
		       person_list[i].last_name, person_list[i].phonenumber);
	    }
	}
    }



  printf ("Information has been removed.");
  fclose (phonebook);
  return 0;
}
