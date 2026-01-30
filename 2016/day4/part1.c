#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define CHECKSUM_LEN 5
#define CHECKSUM_OFF 7
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
	char csum[CHECKSUM_LEN + 1], sid[SECTORID_LEN + 1], counts[ALPHABET_LEN], letters[ALPHABET_LEN];
	int i, j, tmp, match, in, sum = 0;
	size_t len;
	ssize_t read;
	
	csum[CHECKSUM_LEN] = '\0';
	sid[SECTORID_LEN] = '\0';

	while((read = getline(&line, &len, file)) != -1) {
		match = 1;
		memset(counts, 0, sizeof(counts));
		for (i = 0; i < ALPHABET_LEN; i++)
			letters[i] = i + ALPH_OFF;
		
		strncpy(csum, line + read - CHECKSUM_OFF, CHECKSUM_LEN);
		strncpy(sid, line + read - SECTORID_OFF, SECTORID_LEN);

		for (i = 0; i < read - SECTORID_OFF; i++) {
			if (line[i] != '-')
				counts[line[i] - ALPH_OFF]++;
		}

		for (i = 0; i < ALPHABET_LEN; ++i) {
			for (j = 0; j < ALPHABET_LEN - i - 1; j++) {
				if (counts[j] < counts[j + 1]) {
					tmp = counts[j];
					counts[j] = counts[j + 1];
					counts[j + 1] = tmp;
					tmp = letters[j];
					letters[j] = letters[j + 1];
					letters[j + 1] = tmp;
				}
			}
		}

		for (i = 0; i < CHECKSUM_LEN; i++) {
			in = 0;
			for (j = 0; j < CHECKSUM_LEN; j++) {
				if (letters[i] == csum[j]) {
					in = 1;
					break;
				}
			}
			if (in == 0) {
				match = 0;
				break;
			}
		}

		if (match)
			sum += atoi(sid);
	}

	printf("%d\n", sum);

	free(line);
	fclose(file);
	return 0;
}
