#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define WINDOW_LEN 4

int is_valid_palindrome(char *s, int len) {
	// Check it's not the same letter repeated 4 times
	if (s[0] == s[1])
		return 0;

	int b = 0, e = len - 1;
	while (b < e) {
		// Valid palindrome can't contain brackets
		if (s[b] =='[' || s[b] == ']')
			return 0;
		if (s[b] != s[e])
			return 0;
		b++;
		e--;
	}

	return 1;
}

int main(int argc, char** argv) {
	FILE* file = fopen(argv[1], "r");
	if (file == NULL) {
		perror("Failed to open file");
		return 1;
	}

	char* line = NULL;
	char window[WINDOW_LEN];
	int i, v, b, total = 0;
	size_t len;
	ssize_t read;

	while((read = getline(&line, &len, file)) != -1) {
		v = 0;
		b = 0;
		for (i = 0; i < read - 4; i++) {
			if (line[i] == '[')
				b++;
			if (line[i] == ']')
				b--;

			strncpy(window, line + i, WINDOW_LEN);
			if (is_valid_palindrome(window, WINDOW_LEN) == 1) {
				if (b > 0) {
					v = 0;
					break;
				}
				else
					v = 1;
			}
		}

		if (v == 1)
			total++;
	}

	printf("%d\n", total);

	free(line);
	fclose(file);
	return 0;
}
