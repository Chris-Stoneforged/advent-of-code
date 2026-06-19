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
		printf("Index out of bounds\n");
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

bool remove_at(struct List* l, unsigned int index) {
	if (index >= l->len) return false;

	--l->len;
	if (index < l->len) {
		unsigned int dst_off = index * l->esize;
		unsigned int src_off = l->len * l->esize;
		memcpy((char*)l->array + dst_off, (char*)l->array + src_off, l->esize);
	}

	return true;
}

bool remove_at_preserve_order(struct List* l, unsigned int index) {
	if (index >= l->len) return false;

	if (index < l->len) {
		unsigned int dst_off = index * l->esize;
		unsigned int src_off = (index + 1) * l->esize;
		unsigned int len = (--l->len - index) * l->esize;
		memmove((char*)l->array + dst_off, (char*)l->array + src_off, len);
	}

	return true;
}
