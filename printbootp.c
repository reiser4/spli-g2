#include <stdio.h>
#include <string.h>

printbootp(unsigned char op, unsigned char htype, unsigned char hlen, unsigned char hops, const unsigned char *xid, const unsigned char *secs, const unsigned char *flags, const unsigned char *ciaddr, const unsigned char *yiaddr, const unsigned char *siaddr, const unsigned char* giaddr, const unsigned char* chaddr, const unsigned char* sname, const unsigned char* file, const unsigned char *options, int len_opt){
	
	int i;

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
	}

	printf("Hardware address length, value: %d\n", hlen);

	printf("Hops, value: %d", hops);
	if(hops == 0)
		printf("; is set to 0 by a client before transmitting a request and used by relay agents to control the forwarding of BOOTP and/or DHCP messages\n");
	else
		printf("\n");
	
	// TODO: da controllare se e' stato stampato correttamente
	printf("Transaction Identifier, value: ");	
	for(i=0; i<4; i++) {
		printf("%d", xid[i]);
	}
	printf("\n");
	
	// TODO: da controllare se e' corretto che il primo valore sia negativo
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

	printf("Lunghezza campo options: %d\n", len_opt);	
	for(i=0; i<len_opt; i++)
		printf("%d", options[i]);
	printf("\n");


	//printf ("Ip del server: "); printip(siaddr); printf("\n);
	
}
