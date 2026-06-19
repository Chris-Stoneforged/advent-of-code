#include <stdlib.h>
#include <stdbool.h>

struct List {
	size_t capacity;
	size_t esize;
	void* array;
	unsigned int len;
};

struct List* new_list(size_t size, size_t esize);
bool list_is_empty(struct List* l);
bool list_is_full(struct List* l);
bool append(struct List* l, const void* e);
bool get_at(struct List* l, unsigned int index, void* result);
bool remove_at(struct List* l, unsigned int index);
bool remove_at_preserve_order(struct List* l, unsigned int index);
void free_list(struct List* l);
