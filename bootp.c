/// FILE DI MAX
#include <stdio.h>
#include <string.h>
char * cutter_(char *dst, char *src, size_t n) {
	int i;
	for ( i=0; src[i]!='\0' && i < n; i++){
		dst[i] = src[i];
	}
	if(n == 1){
		//printf("Entra?\n");
		dst[i] = src[i];
		return &src[i];
	}
	dst[i]='\0';
//	printf("Cutter RETURN: %s\n",&src[i]);
	return &src[i];
} 

void cutter(char *dst, char *src, size_t n){
	strcpy(src,cutter_(dst,src,n));
}
	

void bootp(unsigned char *packet, int len) {
	//int i;
	//for (i = 0; i < len; i++) {
	//	printf("BOOTP %d/%d %d %c\n", i, len, packet[i], packet[i]);
	//}
	//printf("FINE BOOTP\n");

	// PER MAX:

	//char op = packet[0];
	//char htype = packet[1];

	

	
	//printbootp(op, htype, xid...);
	char op, htype, hlen, hops, xid[4], secs[2], flags[2];
	char ciaddr[4], yiaddr[4], siaddr[4], giaddr[4], chaddr[16];
	char sname[64], file[128];
	char options[1024];
	cutter(&op,packet,sizeof(op));
	cutter(&htype,packet,sizeof(htype));
	cutter(&hlen,packet,sizeof(hops));
	cutter(xid,packet,sizeof(xid));
	cutter(secs,packet,sizeof(secs));
	cutter(flags,packet,sizeof(flags));
	cutter(ciaddr,packet,sizeof(ciaddr));
	cutter(yiaddr,packet,sizeof(yiaddr));
	cutter(yiaddr,packet,sizeof(yiaddr));
	cutter(siaddr,packet,sizeof(siaddr));
	cutter(giaddr,packet,sizeof(giaddr));
	cutter(chaddr,packet,sizeof(chaddr));
	cutter(sname,packet,sizeof(sname));
	cutter(file,packet,sizeof(file));
	cutter(options,packet,sizeof(options));


/*	strcpy(packet,cutter(&op,packet,sizeof(op)));
	strcpy(packet,cutter(&htype,packet,sizeof(htype)));
	strcpy(packet,cutter(&hlen,packet,sizeof(hlen)));
	strcpy(packet,cutter(&hops,packe,sizeof(hops)));
	strcpy(packet,cutter(
	strcpy(variab,parola);
*/
}
