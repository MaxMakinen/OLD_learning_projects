*This project is in finnish.
This is a simple school project where the task was to make a phonebook file that checks if the input information exists in the file, 
if they´re there they get deleted. Otherwise it outputs that "the person that you´re loking for was not in the file".
*/


#include <stdio.h> 
#include <string.h>

int vertaa(char a[20],char b[20],char c[20],char d[20]);

int main(void)    
{  
	int i, val, poistettava = 10, vertaus, suku_vertaus;
	FILE *puhelinluettelo;
	char luettelo[] = "luettelo.txt";
	char maara[3], pois_etunimi[20], pois_sukunimi[20];
	
	
	struct henkilo {
	char etunimi[20];
	char sukunimi[20];
	char puhelinnumero[20];
	};
	struct henkilo henkilo_lista[4];
	
	printf("Anna etunimi:");
	scanf("%s", pois_etunimi);
	printf("Anna sukunimi:");
	scanf("%s", pois_sukunimi);	
	

	if((puhelinluettelo = fopen(luettelo, "r")) == NULL) { 
		printf("Tiedostoa ei löydetty!"); return 0;
	} 
	else {
		for(i=0; i<4; i++) {
			if(i == 0) {
				fscanf(puhelinluettelo, "%s%s%s%s", maara, henkilo_lista[i].etunimi, henkilo_lista[i].sukunimi, henkilo_lista[i].puhelinnumero);
				val = atoi(maara);
			}
			else{
				fscanf(puhelinluettelo, "%s%s%s", henkilo_lista[i].etunimi, henkilo_lista[i].sukunimi, henkilo_lista[i].puhelinnumero);
			}
		}
	}
	
	for(i=0; i<4; i++) {
		vertaus = strcmp(pois_etunimi, henkilo_lista[i].etunimi);
		suku_vertaus = strcmp(pois_sukunimi, henkilo_lista[i].sukunimi);
		if(vertaus == 0){
			if(suku_vertaus == 0){
				poistettava = i;
			}
			else{
			continue;
			}
		}
		else{
		continue;
		}
	}
	
	if(poistettava == 10) {
		printf("Etsimääsi henkilöä ei löytynyt luettelosta.");
		return 0;
	}
	else{
		for(i=0; i<4; i++) {
			if(i == poistettava){
			continue;
			}
			else if(i == 0) {
				val = --val;
				fprintf(puhelinluettelo, "%d%s%s%s", val, henkilo_lista[i].etunimi, henkilo_lista[i].sukunimi, henkilo_lista[i].puhelinnumero);
			}
			else{
				fprintf(puhelinluettelo, "%s%s%s", henkilo_lista[i].etunimi, henkilo_lista[i].sukunimi, henkilo_lista[i].puhelinnumero);
			}
		}
	}
	


	printf("Tiedot poistettu luettelosta.");	
	fclose(puhelinluettelo);	
	return 0;
}

