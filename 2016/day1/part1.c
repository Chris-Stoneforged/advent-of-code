#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char** argv) {
	FILE* file = fopen(argv[1], "r");
	if (file == NULL) {
		perror("Failed to open file");
		return 1;
	}

	char curr, *line = NULL, *instruction;
	size_t len;
	ssize_t read;
	int x = 0, y = 0, dir = 0, dist;
	
	read = getline(&line, &len, file);
	instruction = strtok(line, ", ");

	while (instruction != NULL) {
		curr = instruction[0];
		dist = atoi(&instruction[1]);
		dir = (dir + (curr == 'L' ? -1 : 1) + 4) % 4;

		if (dir == 0) y += dist; // North
		if (dir == 2) y -= dist; // South
		if (dir == 1) x += dist; // East
		if (dir == 3) x -= dist; // West

		instruction = strtok(NULL, ", ");
	}

	printf("%d\n", abs(x) + abs(y));

	free(line);
	fclose(file);
	return 0;
}
