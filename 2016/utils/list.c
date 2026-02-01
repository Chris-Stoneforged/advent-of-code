#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include "list.h"

struct List* new_list(size_t size, size_t esize) {
	struct List* l = malloc(sizeof(struct List));
	if (!l) {
		return NULL;
	}
	
	void* arr = malloc(size * esize);
	if (!arr) {
		free(l);
		return NULL;
	}

	l->len = 0;
	l->capacity = size;
	l->esize = esize;
	l->array = arr;

	return l;
}

bool list_is_empty(struct List* l) {
	return l->len == 0;
}

bool list_is_full(struct List* l) {
	return l->len == l->capacity;
}

bool append(struct List* l, const void* e) {
	if (list_is_full(l)) {
		printf("Cannot append. List is full!\n");
		return false;
	}

	unsigned int off = l->len * l->esize;
	memcpy((char*)l->array + off, e, l->esize);
	++l->len;
	return true;
}

bool get_at(struct List* l, unsigned int index, void* result) {
	if (index >= l->len) {
		printf("Index out of bounds");
		return false;
	}

	unsigned int off = index * l->esize;
	memcpy(result, (char*)l->array + off, l->esize);
	return true;
}

void free_list(struct List* l) {
	free(l->array);
	free(l);
}
