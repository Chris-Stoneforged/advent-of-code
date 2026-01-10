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
	char number[3][5]; // 3 numbers, each taking 5 spaces in the input
	size_t len;
	ssize_t read;
	int s1, s2, s3, i, p = 0;
	
	// Each line has 16 characters, 3 occurances of at least 2 white spaces then a max 3 digit number, and ending with a newline character
	// Ignoring the first white space, we take the last 15 characters and put them in a 3x5 array with the rows representing each number
	// We end up with at least one leading whitespace followed by a trailing whitespace for each array entry (except the last where it's a trailing newline)
	// By replacing the trailing character with a null terminator and the leading whitespace with '0', we can then atoi each array element to get the number
	//   146   94  313			Original string
	//  |---||---||---|			Divide into array
	//  "0146\0", "0094\0", "0313\0"	Replace whitespace
	//  146, 94, 313			atoi
	while((read = getline(&line, &len, file)) != -1) {
		strncpy((char*)number, line + 1, 15);
		for (i = 0; i < 15; i++) {
			if ((i + 1) % 5 == 0)
				((char*)number)[i] = '\0';
			else if (((char*)number)[i] == ' ')
				((char*)number)[i] = '0';
		}

		s1 = atoi(number[0]);
		s2 = atoi(number[1]);
		s3 = atoi(number[2]);
		if (s1 + s2 > s3 && s2 + s3 > s1 && s1 + s3 > s2)
			p++;
	}

	printf("%d\n", p);

	free(line);
	fclose(file);
	return 0;
}
