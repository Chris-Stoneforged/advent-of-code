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
	char number[3][3][5];
	size_t len;
	ssize_t read;
	int s1, s2, s3;
	int i, c = 0, p = 0;
	int u, l;
	
	while((read = getline(&line, &len, file)) != -1) {
		l = c * 15;
		u = l + 15;

		strncpy(((char*)number) + l, line + 1, 15);
		for (i = l; i < u; i++) {
			if ((i + 1) % 5 == 0)
				((char*)number)[i] = '\0';
			else if (((char*)number)[i] == ' ')
				((char*)number)[i] = '0';
		}
		
		if (c < 2) {
			c++;
			continue;
		}

		for (i = 0; i < 3; i++) {
			s1 = atoi(number[0][i]);
			s2 = atoi(number[1][i]);
			s3 = atoi(number[2][i]);
			printf("%d, %d, %d\n", s1, s2, s3);
			if (s1 + s2 > s3 && s2 + s3 > s1 && s1 + s3 > s2)
				p++;
		}

		c = 0;
	}

	printf("%d\n", p);

	free(line);
	fclose(file);
	return 0;
}
