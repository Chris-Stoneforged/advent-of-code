#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int is_valid_aba(char *s) {
	if (s[0] == '[' || s[0] == ']' || s[1] == '[' || s[1] == ']')
		return 0;
	if (s[0] == s[2] && s[0] != s[1])
		return 1;
	return 0;
}

int is_inverse(char* a, char* b) {
	if (a[0] == b[1] && b[0] == a[1])
		return 1;
	return 0;
}

int main(int argc, char** argv) {
	FILE* file = fopen(argv[1], "r");
	if (file == NULL) {
		perror("Failed to open file");
		return 1;
	}

	char* line = NULL;
	char window[3], abas[10][3], babs[10][3];
	int i, j, k, b, v, num_abas, num_babs, total = 0;
	size_t len;
	ssize_t read;

	while((read = getline(&line, &len, file)) != -1) {
		b = 0;
		num_abas = 0;
		num_babs = 0;
		memset(abas, 0, sizeof(abas));
		memset(babs, 0, sizeof(babs));

		for (i = 0; i < read - 3; i++) {
			if (line[i] == '[') {
				b++;
				continue;
			}
			if (line[i] == ']') {
				b--;
				continue;
			}

			strncpy(window, line + i, 3);
			if (is_valid_aba(window) == 1) {
				if (b == 0) {
					strncpy(abas[num_abas], window, 3);
					num_abas++;
				}
				else {
					strncpy(babs[num_babs], window, 3);
					num_babs++;
				}
			}

		}

		for (i = 0; i < num_abas; i++) {
			v = 0;
			for (j = 0; j < num_babs; j++) {
				if (is_inverse(abas[i], babs[j]) == 1) {
					v = 1;
					break;
				}
			}
			if (v == 1) {
				total++;
				break;
			}
		}
	}

	printf("%d\n", total);

	free(line);
	fclose(file);
	return 0;
}
