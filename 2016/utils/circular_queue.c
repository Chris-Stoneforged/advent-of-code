#include "./circular_queue.h"
#include <stdio.h>
#include <assert.h>
#include <string.h>

int round_down_power_of_two(int n) {
	n |= n >> 1;
	n |= n >> 2;
	n |= n >> 4;
	n |= n >> 8;
	n |= n >> 16;
	return (n + 1) >> 1;
}

struct CircularQueue* new_queue(unsigned int size, size_t esize) {
	size = round_down_power_of_two(size);

	struct CircularQueue *q = malloc(sizeof(struct CircularQueue));
	if (!q) return NULL;

	void* arr = malloc(esize * size);
	if (!arr) {
		free(q);
		return NULL;
	}

	q->array = arr;
	q->mask = size - 1;
	q->back = 0;
	q->front = 0;
	q->esize = esize;
	return q;
}

bool queue_is_empty(const struct CircularQueue *q) {
	return q->front == q->back;
}

bool queue_is_full(const struct CircularQueue *q) {
	return q->back - q->front == q->mask + 1;
}

bool enqueue(struct CircularQueue *q, void *item) {
	if (queue_is_full(q)) {
		printf("Cannot enqueue, queue is full\n");
		return false;
	}

	unsigned int off = q->back & q->mask;
	off *= q->esize;
	memcpy((char *)q->array + off, item, q->esize);
	q->back++;
	return true;
}

bool dequeue(struct CircularQueue *q, void *result) {
	if (queue_is_empty(q)) {
		printf("Cannot dequeue from empty queue\n");
		return false;
	}

	unsigned int off = q->front & q->mask;
	off *= q->esize;

	memcpy(result, (char *)q->array + off, q->esize);
	q->front++;
	return true;
}

void free_queue(struct CircularQueue* q) {
	free(q->array);
	free(q);
}
