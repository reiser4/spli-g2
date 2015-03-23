#include <stdio.h>

//#define DEBUG


printbootp(unsigned char op, unsigned char htype, unsigned char hlen, unsigned char hops, const unsigned char *xid, const unsigned char *secs, const unsigned char *flags, const unsigned char *ciaddr, const unsigned char *yiaddr, const unsigned char *siaddr, const unsigned char* giaddr, const unsigned char* chaddr, const unsigned char* sname, const unsigned char* file, const unsigned char *options, int len_opt){
	
	int i, i_opt, len, y, value, n_addr;

	if(op == 1)
		printf("Message op code / message type, value: %d -> BOOTREQUEST\n", op);
	else
		printf("Message op code / message type, value: %d -> BOOTREPLY\n", op);
	
	switch(htype) {
		case 1:
			printf("Hardware address type, value: %d -> Ethernet (10 Mb)\n", htype);
			break;
		case 6:
			printf("Hardware address type, value: %d -> IEEE 802 Networks\n", htype);
			break;
		case 7:
			printf("Hardware address type, value: %d -> ARCNET\n", htype);
			break;
		case 11:
			printf("Hardware address type, value: %d -> LocalTalk\n", htype);
			break;
		case 12:
			printf("Hardware address type, value: %d -> LocalNet (IBM PCNet or SYTEK LocalNET\n", htype);
			break;
		case 14:
			printf("Hardware address type, value: %d -> SMDS\n", htype);
			break;
		case 15:
			printf("Hardware address type, value: %d -> Frame Relay\n", htype);
			break;
		case 16:
			printf("Hardware address type, value: %d -> Asynchronous Transfer Mode (ATM)\n", htype);
			break;
		case 17:
			printf("Hardware address type, value: %d -> HDLC\n", htype);
			break;
		case 18:
			printf("Hardware address type, value: %d -> Fibre Channel\n", htype);
			break;
		case 19:
			printf("Hardware address type, value: %d -> Asynchronous Transfer Mode (ATM)\n", htype);
			break;
		case 20:
			printf("Hardware address type, value: %d -> Serial Line\n", htype);
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

	printf("Flags, value broadcast flag (1 bit): ");
	for(i=0; i<8; i++) {
		printf("%d", flags[0] & (1 << (8-i)));
		if(i<1)
			printf(" - value reserved (15 bit): ");
	}
	printf(" ");
	for(i=0; i<8; i++) {
		printf("%d", !!((flags[1] << i) & 0x80));
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
				printf("Subnet Mask: ");
				for(; i<i_opt; i++) {
					// Print ip
					printf("%d", options[i]);
					if(i<(i_opt-1))
						printf(".");
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
				printf("Router Option (%d address): ", n_addr);
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
				printf("Domain Name Server (%d address): ", n_addr);
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
				printf("Host Name Option: ");
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
				printf("Domain Name (%d address): ", n_addr);
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
				printf("NetBIOS over TCP/IP Name Server Option (%d address): ", n_addr);
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
				i= i_opt;
				printf("NetBIOS over TCP/IP Node Type Option: ");
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
				printf("Requested IP Address: ");
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
				
				printf("IP Address Lease Time: ");
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
				printf("DHCP Message Type: ");
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
				printf("Server identifier: ");
				for(; i<i_opt; i++) {
/*
#ifdef DEBUG
					printf("\n Valore i_opt: %d\n", i_opt);
					printf("Valore i: %d\n", i);
#endif*/
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
				printf("Parameter request list (%d parameters): ", len);
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
				printf("Maximum DHCP message size: ");
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
				printf("Client-identifier (type: %d): ", options[i_opt]);
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
				printf("End Option, value: %d\n", options[i_opt]);
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
