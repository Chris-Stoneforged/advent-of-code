#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define NUM_BOTS 300
#define NUM_OUTPUTS 300
#define BUF_LEN 7

struct Bot {
	int value1, high, low;
	char high_target[BUF_LEN], low_target[BUF_LEN];
};

void give_to_bot(struct Bot bots[NUM_BOTS], int outputs[NUM_OUTPUTS], int bot, int chip) {
	struct Bot *b = &bots[bot];
	if (b->value1 == 0) {
		printf("Bot %d now has chip %d\n", bot, chip);
		b->value1 = chip;
		return;
	}

	printf("Bot %d now has chips %d and %d\n", bot, b->value1, chip);
	int highest = b->value1 > chip ? b->value1 : chip;
	int lowest = b->value1 < chip ? b->value1 : chip;

	if (strcmp(b->high_target, "output") == 0) {
		outputs[b->high] = highest;
	}
	else {
		give_to_bot(bots, outputs, b->high, highest);	
	}

	if (strcmp(b->low_target, "output") == 0) {
		outputs[b->low] = lowest;
	}
	else {
		give_to_bot(bots, outputs, b->low, lowest);
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

	int outputs[NUM_OUTPUTS];
	memset(outputs, 0, sizeof(outputs));

	struct Bot bots[NUM_BOTS];
	memset(bots, 0, sizeof(bots));

	while((read = getline(&line, &len, file)) != -1) {
		printf("%s\n", line);
		if (sscanf(line, v_str, &value, &bot) == 2) {
			give_to_bot(bots, outputs, bot, value);
		}
		else if (sscanf(line, b_str, &bot, low_target, &low, high_target, &high) == 5) {
			set_bot_rules(bots, bot, high_target, high, low_target, low);
		}
	}

	for (int i = 0; i < NUM_OUTPUTS; i++)
		printf("Output %d: %d\n", i, outputs[i]);

	free(line);
	fclose(file);
	return 0;
}
