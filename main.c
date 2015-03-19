#include <stdio.h>
#include <pcap.h>


void
print_payload(const u_char *payload, int len);

/* Returns a string representation of a timestamp. */
const char *timestamp_string(struct timeval ts);

/* Report a problem with dumping the packet with the given timestamp. */
void problem_pkt(struct timeval ts, const char *reason);

/* Report the specific problem of a packet being too short. */
void too_short(struct timeval ts, const char *truncated_hdr);

int main(int argc, char *argv[])
{

	int live = 0;

	char *dev, errbuf[PCAP_ERRBUF_SIZE];
	 pcap_t *handle;
		const u_char *packet;		/* The actual packet */
	struct pcap_pkthdr header;	/* The header that pcap gives us */
		struct bpf_program fp;		/* The compiled filter */
	char filter_exp[] = "udp and (port 68 or port 67)";	/* The filter expression */
		bpf_u_int32 net;		/* Our IP */

	int num_packets = -1;

	dev = pcap_lookupdev(errbuf);
	if (dev == NULL) {
		fprintf(stderr, "Couldn't find default device: %s\n", errbuf);
		return(2);
	}
	printf("Device: %s, bufsiz: %i\n", dev, BUFSIZ);

	if (live == 1) {
		handle = pcap_open_live(dev, BUFSIZ, 1, 1000, errbuf);
		if (handle == NULL) {
			fprintf(stderr, "Couldn't open device %s: %s\n", dev, errbuf);
			return(2);
	 	}
	} else {
                handle = pcap_open_offline("cattura0", errbuf);
	}

	/* Compile and apply the filter */
	if (pcap_compile(handle, &fp, filter_exp, 0, net) == -1) {
		fprintf(stderr, "Couldn't parse filter %s: %s\n", filter_exp, pcap_geterr(handle));
		return(2);
	}
	if (pcap_setfilter(handle, &fp) == -1) {
		fprintf(stderr, "Couldn't install filter %s: %s\n", filter_exp, pcap_geterr(handle));
		return(2);
	}



	/* now we can set our callback function */
	////pcap_loop(handle, num_packets, got_packet, NULL);

	while ((packet = pcap_next(handle, &header)) != NULL)
		got_packet(packet, header.ts, header.caplen);

	/* cleanup */
	pcap_freecode(&fp);
	pcap_close(handle);

	printf("\nCapture complete.\n");



	return(0);
}
