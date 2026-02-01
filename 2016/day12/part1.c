#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "../utils/list.h"

#define INSTRUCTION_LEN 10

int main(int argc, char** argv) {
	FILE *file = fopen(argv[1], "r");
	if (file == NULL) {
		perror("Failed to open file");
		return 1;
	}

	char *line = NULL;
	size_t len;
	ssize_t read;

	const char* ins_fmt = "%s %s %s";
	struct List* instructions = new_list(100, sizeof(char) * INSTRUCTION_LEN);
	int curr = 0, jmp;
	int reg[4];
	char op[4], rhs[3], lhs[3];
	char buf[INSTRUCTION_LEN];

	memset(reg, 0, sizeof(reg));

	while((read = getline(&line, &len, file)) != -1) {
		memset(buf, 0, sizeof(buf));
		unsigned long s_len = strlen(line);
		memcpy(buf, line, s_len - 1);
		buf[s_len] = '\0';
		append(instructions, &buf);
	}

	char curr_ins[INSTRUCTION_LEN];
	while (curr < instructions->len) {
		get_at(instructions, curr, &curr_ins);
		sscanf(curr_ins, ins_fmt, op, lhs, rhs);

		jmp = 1;
		if (strcmp(op, "inc") == 0) {
			++reg[lhs[0] - 97];
		}
		else if (strcmp(op, "dec") == 0) {
			--reg[lhs[0] - 97];
		}
		else if (strcmp(op, "jnz") == 0) {
			if (reg[lhs[0] - 97] != 0) {
				jmp = atoi(rhs);
			}
		}
		else if (strcmp(op, "cpy") == 0) {
			if (lhs[0] == 'a' || lhs[0] == 'b' || lhs[0] == 'c' || lhs[0] == 'd') {
				reg[rhs[0] - 97] = reg[lhs[0] - 97];
			}
			else {
				reg[rhs[0] - 97] = atoi(lhs);
			}
		}

		curr += jmp;
	}

	printf("%d\n", reg[0]);

	free(line);
	fclose(file);
	return 0;
}
