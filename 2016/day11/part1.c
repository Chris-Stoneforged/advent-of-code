#include <stdio.h>
#include <stdlib.h>
#include "utils/circular_queue.h"

int main(int argc, char** argv) {
	FILE *file = fopen(argv[1], "r");
	if (file == NULL) {
		perror("Failed to open file");
		return 1;
	}

	char *line = NULL;
	size_t len;
	ssize_t read;

	long in = 4;
	long out;
	struct CircularQueue *q = new_queue(4, sizeof(long));
	enqueue(q, &in);
	dequeue(q, &out);
	printf("Dequeued %ld\n", (long)out);

	while((read = getline(&line, &len, file)) != -1) {
		printf("%s", line);
	}

	free(q);
	free(line);
	fclose(file);
	return 0;
}
