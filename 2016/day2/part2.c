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
	int col = 3, row = 3, i, c = 0;
	char code[NUM_LINES];
	char keypad[7][7] = {
		' ', ' ', ' ', ' ', ' ', ' ', ' ', 
		' ', ' ', ' ', '1', ' ', ' ', ' ',
		' ', ' ', '2', '3', '4', ' ', ' ',
		' ', '5', '6', '7', '8', '9', ' ',
		' ', ' ', 'A', 'B', 'C', ' ', ' ',
		' ', ' ', ' ', 'D', ' ', ' ', ' ',
		' ', ' ', ' ', ' ', ' ', ' ', ' ', 
	};
	
	while((read = getline(&line, &len, file)) != -1) {
		for (i = 0; i < read - 1; i++) { // - 1 to discard newline
			if (line[i] == 'R') col = keypad[row][col + 1] == ' ' ? col : col + 1;
			if (line[i] == 'L') col = keypad[row][col - 1] == ' ' ? col : col - 1;
			if (line[i] == 'D') row = keypad[row + 1][col] == ' ' ? row : row + 1;
			if (line[i] == 'U') row = keypad[row - 1][col] == ' ' ? row : row - 1;
		}

		code[c] = keypad[row][col];
		c++;
	}

	for (i = 0; i < NUM_LINES; i++)
		printf("%c", code[i]);
	printf("\n");

	free(line);
	fclose(file);
	return 0;
}
