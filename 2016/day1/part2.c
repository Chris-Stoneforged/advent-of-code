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
	int x = 0, y = 0, dir = 0, c = 0, i, dist, hash;
	int visited[1000];
	
	read = getline(&line, &len, file);
	instruction = strtok(line, ", ");

	while (instruction != NULL) {
		curr = instruction[0];
		dist = atoi(&instruction[1]);
		dir = (dir + (curr == 'L' ? -1 : 1) + 4) % 4;

		for (i = 0; i < dist; i++) {
			if (dir == 0) y++;
			if (dir == 2) y--;
			if (dir == 1) x++;
			if (dir == 3) x--;

			hash = (x * 1000) + y;
			for (int i = 0; i < c; i++) {
				if (visited[i] == hash) {
					goto ex;
				}
			}

			visited[c++] = hash;
		}

		instruction = strtok(NULL, ", ");
	}

ex:
	printf("%d\n", abs(x) + abs(y));

	free(line);
	fclose(file);
	return 0;
}
