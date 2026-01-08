#include <stdio.h>
#include <stdlib.h>

int main(int argc, char** argv) {
	FILE* file = fopen(argv[1], "r");
	if (file == NULL) {
		perror("Failed to open file");
		return 1;
	}

	char* line = NULL;
	size_t len;
	ssize_t read;
	
	while((read = getline(&line, &len, file)) != -1) {
		printf("%s", line);
	}

	free(line);
	fclose(file);
	return 0;
}
