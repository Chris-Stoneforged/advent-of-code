#include <stdio.h>
#include <stdlib.h>
#include "../utils/md5.h"

int main(int argc, char **argv) {
	char input[40], password[9], output[9];
	unsigned int suffix = 0, found = 0, i, pos;
	uint8_t result[16];

	memset(password, 0, sizeof(password));
	password[8] = '\0';

	while (found < 8) {
		sprintf(input, "uqwqemis%d", suffix++);
		md5String(input, result);

		if (result[0] == 0 && result[1] == 0) {
			if (result[2] < 8 && password[result[2]] == 0) {
				found++;
				sprintf(output, "%02x", result[3]);
				password[result[2]] = output[0];
			}
		}
	}	

	printf("Password = %s\n", password);
}
