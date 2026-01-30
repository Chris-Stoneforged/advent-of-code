#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "../utils/circular_queue.h"

#define NUM_BOTS 300
#define NUM_OUTPUTS 300
#define BUF_LEN 7

struct Instruction {
	int bot;
	int value;
};

struct Bot {
	int value1, high, low;
	char high_target[BUF_LEN], low_target[BUF_LEN];
};

void give_to_bot(struct Bot bots[NUM_BOTS], int bot, int chip) {
	struct Bot *b = &bots[bot];
	if (b->value1 == 0) {
		b->value1 = chip;
		return;
	}

	if ((b->value1 == 61 && chip == 17) || (b->value1 == 17 && chip == 61)) {
		printf("%d\n", bot);
	}

	int highest = b->value1 > chip ? b->value1 : chip;
	int lowest = b->value1 < chip ? b->value1 : chip;

	if (strcmp(b->high_target, "bot") == 0) {
		give_to_bot(bots, b->high, highest);	
	}

	if (strcmp(b->low_target, "bot") == 0) {
		give_to_bot(bots, b->low, lowest);
	}
}

void set_bot_rules(struct Bot bots[NUM_BOTS], int bot, char h_t[BUF_LEN], int h, char l_t[BUF_LEN], int l) {
	strncpy(bots[bot].high_target, h_t, BUF_LEN);
	strncpy(bots[bot].low_target, l_t, BUF_LEN);
	bots[bot].high = h;
	bots[bot].low = l; 
}

int main(int argc, char** argv) {
	FILE *file = fopen(argv[1], "r");
	if (file == NULL) {
		perror("Failed to open file");
		return 1;
	}

	char *line = NULL;
	size_t len = 0;
	ssize_t read;
	
	char *v_str = "value %d goes to bot %d", *b_str = "bot %d gives low to %s %d and high to %s %d";
	char high_target[BUF_LEN], low_target[BUF_LEN];
	int value, bot, high, low;

	struct CircularQueue* q = new_queue(256, sizeof(struct Instruction));

	struct Bot bots[NUM_BOTS];
	memset(bots, 0, sizeof(bots));

	while((read = getline(&line, &len, file)) != -1) {
		if (sscanf(line, v_str, &value, &bot) == 2) {
			struct Instruction i = { bot, value};
			enqueue(q, &i);
		}
		else if (sscanf(line, b_str, &bot, low_target, &low, high_target, &high) == 5) {
			set_bot_rules(bots, bot, high_target, high, low_target, low);
		}
	}

	struct Instruction i; 
	while (!is_empty(q)) {
		dequeue(q, &i);
		give_to_bot(bots, i.bot, i.value);
	}

	free(line);
	fclose(file);
	return 0;
}
