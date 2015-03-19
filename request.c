

void request(unsigned char *packet, int len) {
	int i;
	for (i = 0; i < len; i++) {
		printf("REQUEST %d/%d %d %c\n", i, len, packet[i], packet[i]);
	}
	printf("FINE REQUEST\n");
}