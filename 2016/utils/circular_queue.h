#include <stdbool.h>
#include <stdlib.h>

struct CircularQueue {
	void* array;
	size_t esize;
	unsigned int mask;
	unsigned int back;
	unsigned int front;
};

struct CircularQueue* new_queue(unsigned int size, size_t esize);
bool is_empty(const struct CircularQueue *q);
bool is_full(const struct CircularQueue *q);
bool enqueue(struct CircularQueue *q, void *item);
bool dequeue(struct CircularQueue *q, void *result);
