#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include "../utils/md5.h"
#include "../utils/list.h"

struct PendingKey {
	int i, f; 
	char c;
	char hash[33];
};

char has_triple(char hash[32]) {
	for (int i = 2; i < 32; ++i) {
		if (hash[i] == hash[i - 1] && hash[i] == hash[i - 2])
			return hash[i];
	}
	return 0;
}

bool has_pentuple(char hash[32], char c) {
	for (int i = 4; i < 32; ++i) {
		if (hash[i] == c && hash[i - 1] == c && hash[i - 2] == c && hash[i - 3] == c && hash[i - 4] == c)
			return true;
	}
	return false;
}

int main(int argc, char** argv) {
	char input[40], output[32];
	int index = 0, keys = 0, i, last = 0;
	char c;
	uint8_t result[16];
	struct List* pks = new_list(1000, sizeof(struct PendingKey));
	struct PendingKey pk;

	while (keys < 64) {
		sprintf(input, "cuanljph%d", index);
		md5String(input, result);

		for (i = 0; i < 16; ++i)
			sprintf(output + (i * 2), "%02x", result[i]);

		for (i = pks->len - 1; i >= 0; --i) {
			get_at(pks, i, &pk);
			if (index - 1000 > pk.i) {
				remove_at_preserve_order(pks, i);
				continue;
			}
			if (has_pentuple(output, pk.c)) {
				printf("Found pentuple (%s) at %d for pk %d - %s. This is a key.\n", output, index, pk.i, pk.hash);
				++keys;
				if (pk.i > last)
					last = pk.i;
				remove_at_preserve_order(pks, i);
			}
		}

		if ((c = has_triple(output)) != 0) {
			struct PendingKey pk = { index, 0, c };
			memcpy(&pk.hash, &output, 33);
			append(pks, &pk);
		}

		++index;
	}	

	printf("64th key produced at index %d\n", last);
	free_list(pks);
	return 0;
}
