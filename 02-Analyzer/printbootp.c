#include <stdio.h>

//#define DEBUG


printbootp(unsigned char op, unsigned char htype, unsigned char hlen, unsigned char hops, const unsigned char *xid, const unsigned char *secs, const unsigned char *flags, const unsigned char *ciaddr, const unsigned char *yiaddr, const unsigned char *siaddr, const unsigned char* giaddr, const unsigned char* chaddr, const unsigned char* sname, const unsigned char* file, const unsigned char *options, int len_opt){
	
	int i, i_opt, len, y, value, n_addr;

	if(op == 1)
		printf("Message op code / message type, value: %d -> BOOTREQUEST\n", op);
	else
		printf("Message op code / message type, value: %d -> BOOTREPLY\n", op);
	printf("Hardware address type, value: ");
	switch(htype) {
		case 1:
			printf(" %d -> Ethernet (10 Mb)\n", htype);
			break;
		case 6:
			printf(" %d -> IEEE 802 Networks\n", htype);
			break;
		case 7:
			printf(" %d -> ARCNET\n", htype);
			break;
		case 11:
			printf(" %d -> LocalTalk\n", htype);
			break;
		case 12:
			printf(" %d -> LocalNet (IBM PCNet or SYTEK LocalNET\n", htype);
			break;
		case 14:
			printf(" %d -> SMDS\n", htype);
			break;
		case 15:
			printf(" %d -> Frame Relay\n", htype);
			break;
		case 16:
			printf(" %d -> Asynchronous Transfer Mode (ATM)\n", htype);
			break;
		case 17:
			printf(" %d -> HDLC\n", htype);
			break;
		case 18:
			printf(" %d -> Fibre Channel\n", htype);
			break;
		case 19:
			printf(" %d -> Asynchronous Transfer Mode (ATM)\n", htype);
			break;
		case 20:
			printf(" %d -> Serial Line\n", htype);
			break;
		default:
			printf("ERRORE: switch htype");
			break;
	}

	printf("Hardware address length, value: %d\n", hlen);

	printf("Hops, value: %d", hops);
	if(hops == 0)
		printf("; is set to 0 by a client before transmitting a request and used by relay agents to control the forwarding of BOOTP and/or DHCP messages\n");
	else
		printf("\n");
	
	printf("Transaction Identifier, value: ");	
	for(i=0; i<4; i++) {
		printf("%d", xid[i]);
	}
	printf("\n");
	
	printf("Seconds elapsed since client began address acquisition or renewal process, values: %d - %d\n", secs[0], secs[1]);

	// TODO: stampare bit
	printf("flags[0]: %d, flags[1]: %d\n", flags[0], flags[1]);
	printf("Flags, value broadcast flag (1 bit): ");
	for(i=0; i<8; i++) {
		printf("%d-", flags[0] & (1 << (8-i)));
		/*if(i<1)
			printf(" - value reserved (15 bit): ");
		else
			printf("-");*/
	}
	printf("\n");
	
	printf("Client IP address: ");
	printip(ciaddr);	
	
	printf("'Your' IP Address: ");
	printip(yiaddr);

	printf("Server IP Address: ");	
	printip(siaddr);

	printf("Gateway IP Address: ");
	printip(giaddr);
	
	printf("Client hardware address: ");
	for(i=0; i<16; i++) {
		printf("%d", chaddr[i]);
		if(i<15)
			printf(":");
		else
			printf("\n");
	}

	printf("Server Name: ");
	for(i=0; i<64; i++)
		printf("%d", sname[i]);
	printf("\n");
	
	printf("Boot Filename: ");
	for(i=0; i<128; i++)
		printf("%d", file[i]);
	printf("\n");

#ifdef DEBUG
	printf("Lunghezza campo options: %d\n", len_opt);	
	for(i=0; i<len_opt; i++)
		printf("%d ", options[i]);
	printf("\n");
#endif

	printf("Print options fields:\n");
	i_opt=0;
	while(i_opt<len_opt) {

#ifdef DEBUG
		
		printf("Valore options (dopo while): %d\n", options[i_opt]);
#endif

		switch(options[i_opt]) {
			case 1:
				// Aumento di uno perche' ho letto il tipo di campo opzionale
				i_opt++;
				len = options[i_opt];
				// aumento di uno perche' ho la lughezza fissa
				i_opt++;
				i= i_opt;
				// Aumento di 4 perche' vado a leggere un indirizzo ip
				i_opt += len;
				printf("\tSubnet Mask: ");
				for(; i<i_opt; i++) {
					// Print ip
					printf("%d", options[i]);
					if(i<(i_opt-1))
						printf(".");
					else
						printf("\n");
				}
				break;
			case 2:
				// Aumento di uno perche' ho letto il tipo di campo opzionale
				i_opt++;
				len = options[i_opt];
				// aumento di uno perche' ho la lughezza fissa
				i_opt++;
				i= i_opt;
				// Aumento di 4 perche' vado a leggere un indirizzo ip
				i_opt += len;
				printf("\tTime Offset: ");
				for(; i<i_opt; i++) {
					// Stampo l'ora UTC;
					printf("%d", options[i]);
					if(i<(i_opt-1))
						printf(":");
					else
						printf("\n");
				}
				break;
			case 3:
				// Aumento di uno perche' ho letto il tipo di campo opzionale
				i_opt++;
				len = options[i_opt];
				// aumento di uno perche' ho la lughezza fissa
				i_opt++;
				i= i_opt;
				// Aumento di n perche' vado a leggere le opzioni del router
				i_opt += len;
				n_addr = len / 4;
				printf("\tRouter Option (%d address): ", n_addr);
				for(; i<i_opt; i++) {
					// Print ip
					printf("%d", options[i]);
					
					if(i<(i_opt-1))
						printf(".");
					else
						printf("\n");
				}
				break;
			case 6:
				// Aumento di uno perche' ho letto il tipo di campo opzionale
				i_opt++;
				len = options[i_opt];
				// aumento di uno perche' ho la lughezza fissa
				i_opt++;
				i= i_opt;
				// Aumento di n perche' vado a leggere n indirizzi ip del router
				i_opt += len;
				n_addr = len / 4;
				printf("\tDomain Name Server (%d address): ", n_addr);
				y=0;
				for(; i<i_opt; i++) {
					y++;
					// Print ip
					printf("%d", options[i]);
					if(y<4) {
						if(i<(i_opt-1))
							printf(".");
					} else {
						y=0;
						printf(" ");
					}
				}
				printf("\n");
				break;
			case 12:
				// Aumento di uno perche' ho letto il tipo di campo opzionale
				i_opt++;
				len = options[i_opt];
				// aumento di uno perche' ho la lughezza fissa
				i_opt++;
				i = i_opt;
				// Aumento di 2 perche' vado a leggere due valori
				i_opt += len;
				printf("\tHost Name Option: ");
				for(; i<i_opt; i++) {
					// Stampo i parametri
					printf("%c", options[i]);
					if(i == (i_opt-1))
						printf("\n");
				}
				break;				
			case 15:
				// Aumento di uno perche' ho letto il tipo di campo opzionale
				i_opt++;
				len = options[i_opt];
				// aumento di uno perche' ho la lughezza fissa
				i_opt++;
				i= i_opt;
				// Aumento di n perche' vado a leggere n indirizzi ip del router
				i_opt += len;
				n_addr = len / 4;
				printf("\tDomain Name (%d address): ", n_addr);
				y=0;
				for(; i<i_opt; i++) {
					y++;
					// Print ip
					printf("%d", options[i]);
					if(y<4) {
						if(i<(i_opt-1))
							printf(".");
					} else {
						y=0;
						printf(" ");
					}
				}
				printf("\n");
				break;
			case 26:
				/* 
					This option specifies the MTU to use on this interface.  The MTU is
					specified as a 16-bit unsigned integer.  The minimum legal value for
					the MTU is 68.
				*/
				// Aumento di uno perche' ho letto il tipo di campo opzionale
				i_opt++;
				len = options[i_opt];
				i = i_opt;
				// aumento di due perche' ho la lughezza fissa
				i_opt += len;
				printf("\tInterface MTU Option: ");
				for(; i<i_opt; i++) {
					printf("%d ", options[i]);
				}
				printf("\n");
				i_opt++;
				break;
			case 42:
				// Aumento di uno perche' ho letto il tipo di campo opzionale
				i_opt++;
				len = options[i_opt];
				// aumento di uno perche' ho la lughezza fissa
				i_opt++;
				i= i_opt;
				// Aumento di n perche' vado a leggere n indirizzi ip del router
				i_opt += len;
				n_addr = len / 4;
				printf("\tNetwork Time Protocol Servers Option (%d address): ", n_addr);
				y=0;
				for(; i<i_opt; i++) {
					y++;
					// Print ip
					printf("%d", options[i]);
					if(y<4) {
						if(i<(i_opt-1))
							printf(".");
					} else {
						y=0;
						printf(" ");
					}
				}
				printf("\n");
				break;				
			case 44:
				// Aumento di uno perche' ho letto il tipo di campo opzionale
				i_opt++;
				len = options[i_opt];
				// aumento di uno perche' ho la lughezza fissa
				i_opt++;
				i= i_opt;
				// Aumento di n perche' vado a leggere n indirizzi ip del router
				i_opt += len;
				n_addr = len / 4;
				printf("\tNetBIOS over TCP/IP Name Server Option (%d address): ", n_addr);
				y=0;
				for(; i<i_opt; i++) {
					y++;
					// Print ip
					printf("%d", options[i]);
					if(y<4) {
						if(i<(i_opt-1))
							printf(".");
					} else {
						y=0;
						printf(" ");
					}
				}
				printf("\n");
				break;
			case 46:
				// Aumento di uno perche' ho letto il tipo di campo opzionale
				i_opt++;
				len = options[i_opt];
				// aumento di uno perche' ho la lughezza fissa
				i_opt++;
				printf("\tNetBIOS over TCP/IP Node Type Option: ");
				switch(options[i_opt]) {
					case 1:
						printf("B-node\n");
						break;
					case 2:
						printf("P-node\n");
						break;
					case 4:
						printf("M-node\n");
						break;
					case 8:
						printf("H-node\n");
						break;
					default:
						printf("ERRORE: case 46\n");
						return(-1);
				}
				i_opt++;
				break;
			case 50:
				// Aumento di uno perche' ho letto il tipo di campo opzionale
				i_opt++;
				len = options[i_opt];
				// aumento di uno perche' ho la lughezza fissa
				i_opt++;
				i= i_opt;
				// Aumento di 4 perche' vado a leggere un indirizzo ip
				i_opt += len;
				printf("\tRequested IP Address: ");
				for(; i<i_opt; i++) {
					// Print ip
					printf("%d", options[i]);
					if(i<(i_opt-1))
						printf(".");
					else
						printf("\n");
				}
				break;
				
			case 51:
				// Aumento di uno perche' ho letto il tipo di campo opzionale
				i_opt++;
				len = options[i_opt];
				// aumento di uno perche' ho la lughezza fissa
				i_opt++;
				i= i_opt;
				// Aumento di 4 perche' vado a leggere un indirizzo ip
				i_opt += len;
				
				printf("\tIP Address Lease Time: ");
				for(; i<i_opt; i++) {
					// Stampo i secondi
					printf("%d", options[i]);
					if(i<(i_opt-1))
						printf("-");
					else
						printf(" seconds\n");
				}
				break;
			case 53:
				// Aggiungo valore
				i_opt++;
				// lunghezza valore fissa = 1
				i_opt++;

#ifdef DEBUG
				printf("Value: %d\n", options[i_opt]);			
#endif

				printf("\tDHCP Message Type: ");
				switch(options[i_opt]) {
					case 1:
						printf("DHCPDISCOVER\n");
						break;
					case 2:
						printf("DHCPOFFER\n");
						break;
					case 3:
						printf("DHCPREQUEST\n");
						break;
					case 4:
						printf("DHCPDECLINE\n");
						break;
					case 5:
						printf("DHCPACK\n");
						break;
					case 6:
						printf("DHCPNAK\n");
						break;
					case 7:
						printf("DHCPRELEASE\n");
						break;
					case 8:
						printf("DHCPINFORM\n");
						break;
					default:
						printf("ERRORE: case 53\n");
						return(-1);
				}
				i_opt++;
				break;
			case 54:
				// Aumento di uno perche' ho letto il tipo di campo opzionale
				i_opt++;
				len = options[i_opt];
				// aumento di uno perche' ho la lughezza fissa
				i_opt++;
				i= i_opt;
				// Aumento di 4 perche' vado a leggere un indirizzo ip
				i_opt += len;
				printf("\tServer identifier: ");
				for(; i<i_opt; i++) {
					// Stampo l'indirizzo ip
					printf("%d", options[i]);
					if(i<(i_opt-1))
						printf(".");
					else
						printf("\n");
				}
				break;
			case 55:
				// Aumento di uno perche' ho letto il tipo di campo opzionale
				i_opt++;
				len = options[i_opt];
				// aumento di uno perche' ho la lughezza fissa
				i_opt++;
				i= i_opt;
				// Aumento di n perche' vado a leggere un indirizzo ip
				i_opt += len;
				printf("\tParameter request list (%d parameters): ", len);
				for(; i<i_opt; i++) {
					// Stampo i parametri di richiesta 
					printf("%d ", options[i]);
					if(i == (i_opt-1))
						printf("\n");
				}
				break;
			case 57:
				// Aumento di uno perche' ho letto il tipo di campo opzionale
				i_opt++;
				len = options[i_opt];
				// aumento di uno perche' ho la lughezza fissa
				i_opt++;
				i = i_opt;
				// Aumento di 2 perche' vado a leggere due valori
				i_opt += len;
				printf("\tMaximum DHCP message size: ");
				for(; i<i_opt; i++) {
					// Stampo i parametri
					printf("%d ", options[i]);
					if(i == (i_opt-1))
						printf("\n");
				}
				break;
			case 61:
				
				// Aumento di uno perche' ho letto il tipo di campo opzionale
				i_opt++;
				len = options[i_opt];
				// aumento di uno perche' ho la lughezza fissa
				i_opt++;
				printf("\tClient-identifier (type: %d): ", options[i_opt]);
				// Aumento di uno perchè ho preso il Type
				i_opt++;
				i = i_opt;
				// Aumento di 2 perche' vado a leggere due valori
				i_opt += (len-1);
				for(; i<i_opt; i++) {
					// Stampo i parametri
					printf("%d ", options[i]);
					if(i == (i_opt-1))
						printf("\n");
				}
				break;
			case 255:
				// Aggiungo valore
				printf("\tEnd Option, value: %d\n", options[i_opt]);
				// Sono arrivato alla fine del campo variabile, per questo motivo esco
				i_opt = len_opt;
				break;
				
			default:
				printf("ERRORE: options fields\n");
				return(-1);
		}
	}

#ifdef DEBUG
	printf ("Sono fuori dal ciclo while\n");
#endif

}
