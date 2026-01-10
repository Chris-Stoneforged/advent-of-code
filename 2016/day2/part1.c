#include <stdio.h>
#include <stdlib.h>

#define NUM_LINES 5

int main(int argc, char** argv) {
	FILE* file = fopen(argv[1], "r");
	if (file == NULL) {
		perror("Failed to open file");
		return 1;
	}

	char* line = NULL;
	size_t len;
	ssize_t read;
	int col = 1, row = 1, i, c = 0;
	int code[NUM_LINES];
	
	while((read = getline(&line, &len, file)) != -1) {
		for (i = 0; i < read - 1; i++) { // - 1 to discard newline
			if (line[i] == 'R') col = col == 2 ? col : col + 1;
			if (line[i] == 'L') col = col == 0 ? col : col - 1;
			if (line[i] == 'D') row = row == 2 ? row : row + 1;
			if (line[i] == 'U') row = row == 0 ? row : row - 1;
		}

		code[c] = row * 3 + col + 1;
		c++;
	}

	for (i = 0; i < NUM_LINES; i++)
		printf("%d", code[i]);
	printf("\n");

	free(line);
	fclose(file);
	return 0;
}
