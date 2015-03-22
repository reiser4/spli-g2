/// FILE DI MAX
#include <stdio.h>
#include <string.h>

#define DEBUG

int len_cost, tot; //inizializzo i contatori

char * dividi(unsigned char *dst, unsigned char *src, size_t );
	
void bootp(unsigned char *packet, int len) {
		
	//int i;
	//for (i = 0; i < len; i++) {
	//	printf("BOOTP %d/%d %d %c\n", i, len, packet[i], packet[i]);
	//}
	//printf("FINE BOOTP\n");

	// PER MAX:

	//char op = packet[0];
	//char htype = packet[1];

	
	len_cost = 0; //azzero i contatori
	tot = len;
	
	int i;
	int len_var;
	/* Stampa pacchetto intero per Debug*/
#ifdef DEBUG
	printf("packet: ");
	for ( i=0; i < len ; i++){
		printf("%d",packet[i]);
	}
	printf("\n");
#endif
	unsigned char op, htype, hlen, hops, xid[4], secs[2], flags[2];
	unsigned char ciaddr[4], yiaddr[4], siaddr[4], giaddr[4], chaddr[16];
	unsigned char sname[64], file[128];
	unsigned char options[1024];
	packet = dividi(&op,packet,sizeof(op));
	packet = dividi(&htype,packet,sizeof(htype));
	packet = dividi(&hlen,packet,sizeof(hlen));
	packet = dividi(&hops,packet,sizeof(hops));
	packet = dividi(xid,packet,sizeof(xid));
	packet = dividi(secs,packet,sizeof(secs));
	packet = dividi(flags,packet,sizeof(flags));
	packet = dividi(ciaddr,packet,sizeof(ciaddr));
	packet = dividi(yiaddr,packet,sizeof(yiaddr));
	packet = dividi(yiaddr,packet,sizeof(yiaddr));
	packet = dividi(siaddr,packet,sizeof(siaddr));
	packet = dividi(giaddr,packet,sizeof(giaddr));
	packet= dividi(chaddr,packet,sizeof(chaddr));
	packet = dividi(sname,packet,sizeof(sname));
	packet = dividi(file,packet,sizeof(file));
	
	len_var = len - len_cost; //calolo la lunghezza di options
	//printf("len_var = len -len_cost: %d = %d - %d\n",len_var,len,len_cost);

	dividi(options,packet,len_var);
	
	
	printbootp(op, htype, hlen, hops, xid, secs, flags, ciaddr, yiaddr, siaddr, giaddr, chaddr,sname, file, options, len_var);

}

char * dividi(unsigned char *dst, unsigned char *src, size_t n){ 
	int i;
	for ( i = 0; i < n; i++) {
		dst[i] = src[i];
#ifdef DEBUG
		printf("%d ",dst[i]);
#endif
	}
#ifdef DEBUG
	printf(" lungo %d\n",i);
#endif
	tot = tot - i;
	len_cost = len_cost + i;
	return &src[i];
}
