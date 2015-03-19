
#include <pcap.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>
#include <errno.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <netinet/in.h>
#include <netinet/ip.h>
#include <net/if.h>
#include <netinet/if_ether.h>

#define SIZE_ETHERNET 14
#define ETHER_ADDR_LEN	6

const char *timestamp_string(struct timeval ts);
void problem_pkt(struct timeval ts, const char *reason);
void too_short(struct timeval ts, const char *truncated_hdr);
void bootreply(unsigned char *packet, int len);

struct UDP_hdr {
	u_short	uh_sport;		/* source port */
	u_short	uh_dport;		/* destination port */
	u_short	uh_ulen;		/* datagram length */
	u_short	uh_sum;			/* datagram checksum */
};

void got_packet(const unsigned char *packet, struct timeval ts,
			unsigned int capture_len) {
	struct ip *ip;
	struct UDP_hdr *udp;
	unsigned int IP_header_length;
	int i, len;
	if (capture_len < sizeof(struct ether_header))
		{
		too_short(ts, "Ethernet header");
		return;
		}

	packet += sizeof(struct ether_header);
	capture_len -= sizeof(struct ether_header);

	if (capture_len < sizeof(struct ip)) {
		too_short(ts, "IP header");
		return;
	}

	ip = (struct ip*) packet;
	IP_header_length = ip->ip_hl * 4;	/* ip_hl is in 4-byte words */

	printf("--------------\n");
	printf("       From: %s\n", inet_ntoa(ip->ip_src));
	printf("         To: %s\n", inet_ntoa(ip->ip_dst));

	if (capture_len < IP_header_length)
		{
		too_short(ts, "IP header with options");
		return;
		}

	if (ip->ip_p != IPPROTO_UDP)
		{
		problem_pkt(ts, "non-UDP packet");
		return;
		}

	packet += IP_header_length;
	capture_len -= IP_header_length;

	if (capture_len < sizeof(struct UDP_hdr))
		{
		too_short(ts, "UDP header");
		return;
		}

	udp = (struct UDP_hdr*) packet;

	printf("%s UDP src_port=%d dst_port=%d length=%d\n",
		timestamp_string(ts),
		ntohs(udp->uh_sport),
		ntohs(udp->uh_dport),
		ntohs(udp->uh_ulen));

	for (i = 8; i < ntohs(udp->uh_ulen); i++) {
		printf("%d/%d %d %c\n", i, ntohs(udp->uh_ulen), packet[i], packet[i]);
	}
	printf("\n");
	len = ntohs(udp->uh_ulen) - 8;
		

	if (packet[8] == 2) {
		bootreply((unsigned char*)packet+8, (int)len);
		return;
	}

	if (packet[8] == 1) {
		request((unsigned char*)packet+8, (int)len);
		return;
	}

	printf("Altro tipo di richiesta... %d\n", packet[8]);



}


void bootreply(unsigned char *packet, int len) {
	int i;
	for (i = 0; i < len; i++) {
		printf("BOOTREPLY %d/%d %d %c\n", i, len, packet[i], packet[i]);
	}
	printf("FINE BOOTREPLY\n");
}


const char *timestamp_string(struct timeval ts) {
	static char timestamp_string_buf[256];

	sprintf(timestamp_string_buf, "%d.%06d",
		(int) ts.tv_sec, (int) ts.tv_usec);

	return timestamp_string_buf;
}

void problem_pkt(struct timeval ts, const char *reason) {
	fprintf(stderr, "%s: %s\n", timestamp_string(ts), reason);
}

void too_short(struct timeval ts, const char *truncated_hdr) {
	fprintf(stderr, "packet with timestamp %s is truncated and lacks a full %s\n",
		timestamp_string(ts), truncated_hdr);
}

