#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char** argv) {
	FILE* file = fopen(argv[1], "r");
	if (file == NULL) {
		perror("Failed to open file");
		return 1;
	}

	char* line = NULL;
	size_t len;
	ssize_t read;
	int total = 0;
	
	read = getline(&line, &len, file);
	for (int i = 0; i < read - 1; i++) {
		if (line[i] != '(') {
			total += 1;
			continue;
		}

		char *a_s = strtok(line + i, "(x)"), *b_s = strtok(NULL, "(x)");
		int a = atoi(a_s), b = atoi(b_s);
		total += a * b;
		i += a + strlen(a_s) + strlen(b_s) + 2;
	}

	printf("%d\n", total);

	free(line);
	fclose(file);
	return 0;
}
