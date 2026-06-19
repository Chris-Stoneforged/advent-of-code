#include <stdio.h>
#include "../utils/list.h"

int main(int argc, char* argv[]) {
	struct List* l = new_list(5, sizeof(int));
	int i = 0, b;

	append(l, &i);
	i++;
	append(l, &i);
	i++;
	append(l, &i);
	i++;
	append(l, &i);

	for (i = 0; i < l->len; ++i) {
		get_at(l, i, &b);
		printf("%d, ", b);
	}
	printf("\n");

	remove_at_preserve_order(l, 3);

	for (i = 0; i < l->len; ++i) {
		get_at(l, i, &b);
		printf("%d, ", b);
	}
	printf("\n");

	return 0;
}
