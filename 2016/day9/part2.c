#include <stdio.h>
#include <stdlib.h>
#include <string.h>

unsigned long evaluate_section(char *section, int len) {
	unsigned long total = 0;
	for (int i = 0; i < len; i++) {
		if (section[i] != '(') {
			total += 1;
			continue;
		}

		char *a_s = strtok(section + i, "(x)"), *b_s = strtok(NULL, "(x)");
		int a = atoi(a_s), b = atoi(b_s);

		char subsection[a];
		int new_offset = i + strlen(a_s) + strlen(b_s) + 3;

		strncpy(subsection, section + new_offset, a);
		total += b * evaluate_section(subsection, a);

		i += a + strlen(a_s) + strlen(b_s) + 2;
		
	}
	return total;
}

int main(int argc, char** argv) {
	FILE *file = fopen(argv[1], "r");
	if (file == NULL) {
		perror("Failed to open file");
		return 1;
	}

	char *line = NULL;
	char *section;
	size_t len;
	ssize_t read;
	int total = 0;
	
	read = getline(&line, &len, file);
	printf("%lu\n", evaluate_section(line, read - 1));

	free(line);
	fclose(file);
	return 0;
}
