#include <stdio.h>

printip(const unsigned char* ip) {

	// dato un array di 4 char stampare l'indirizzo ip in formato leggibile
	// esempio: ip[] = [127, 0, 0, 1];
	// output: "127.0.0.1"
	int i;
	for(i=0; i<4; i++) {
		printf("%d", ip[i]);
		if(i<3)
			printf(".");
		else
			printf("\n");
	}

}
