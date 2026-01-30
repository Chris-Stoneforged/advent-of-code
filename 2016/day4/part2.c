#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define SECTORID_LEN 3
#define SECTORID_OFF 11
#define ALPHABET_LEN 26
#define ALPH_OFF 97

int main(int argc, char** argv) {
	FILE* file = fopen(argv[1], "r");
	if (file == NULL) {
		perror("Failed to open file");
		return 1;
	}

	char* line = NULL;
	char sid[SECTORID_LEN + 1];
	int i, s;
	size_t len;
	ssize_t read;
	
	sid[SECTORID_LEN] = '\0';

	while((read = getline(&line, &len, file)) != -1) {
		strncpy(sid, line + read - SECTORID_OFF, SECTORID_LEN);
		s = atoi(sid);

		for (i = 0; i < read - SECTORID_OFF; i++) {
			if (line[i] == '-')
				printf(" ");
			else
				printf("%c", ((line[i] - ALPH_OFF + s) % ALPHABET_LEN) + ALPH_OFF);

		}
		printf("\t%d\n", s);
	}

	free(line);
	fclose(file);
	return 0;
}
