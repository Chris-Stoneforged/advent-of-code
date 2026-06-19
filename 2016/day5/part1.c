#include <stdio.h>
#include <stdlib.h>
#include "../utils/md5.h"

int main(int argc, char **argv) {
	char input[40], password[9], output[3];
	int suffix = 0, found = 0;
	unsigned int i;
	uint8_t result[16];

	password[8] = '\0';

	while (found < 8) {
		sprintf(input, "uqwqemis%d", suffix++);
		md5String(input, result);
		if (result[0] == 0 && result[1] == 0) {
			sprintf(output, "%02x", result[2]);
			if (output[0] == '0')
				password[found++] = output[1];
		}
	}	

	printf("Password = %s\n", password);
}
