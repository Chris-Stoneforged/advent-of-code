#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define ALPH 26
#define LETTERS 8

int main(int argc, char** argv) {
	FILE* file = fopen(argv[1], "r");
	if (file == NULL) {
		perror("Failed to open file");
		return 1;
	}

	char* line = NULL;
	int counts[LETTERS][ALPH];
	char final[LETTERS + 1];
	size_t len;
	ssize_t read;
	int i, j, frequency_count, most_frequent;

	memset(counts, 0, sizeof(counts));
	while((read = getline(&line, &len, file)) != -1) {
		for (i = 0; i < LETTERS; i++)
			counts[i][line[i]- 97]++;
	}

	for (i = 0; i < LETTERS; i++) {
		frequency_count = 0;
		for (j = 0; j < ALPH; j++) {
			if (counts[i][j] > frequency_count) {
				frequency_count = counts[i][j];
				most_frequent = j;
			}
		}
		final[i] = most_frequent + 97;
	}

	final[LETTERS] = '\0';
	printf("%s\n", final);

	free(line);
	fclose(file);
	return 0;
}
