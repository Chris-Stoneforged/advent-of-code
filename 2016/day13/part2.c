#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <limits.h>
#include "../utils/circular_queue.h"
#include "../utils/list.h"

#define START_X 1
#define START_Y 1
#define GOAL_X 31
#define GOAL_Y 39

struct Position {
	int x, y, moves;
};

int get_binary_ones(int i) {
	int digits = 0, ones = 0;
	for (; 1 << digits <= i; ++digits)
		if (((1 << digits) & i) != 0)
			++ones;
	return ones;
}

bool is_wall(int x, int y) {
	int i = (x*x) + (3*x) + (2*x*y) + y + (y*y) + 1358;
	int ones = get_binary_ones(i);
	return ones % 2 == 1;
}

bool is_valid_space(int x, int y) {
	return x >= 0 && y >= 0 && !is_wall(x, y);
}

bool has_been_visited(struct List* visited, int x, int y) {
	struct Position p;
	for (int i = 0; i < visited->len; ++i) {
		get_at(visited, i, &p);
		if (p.x == x && p.y == y) return true;
	}
	return false;
}

void enqueue_neighbour(struct CircularQueue* q, struct List* visited, int x, int y, int moves) {
	if (!is_valid_space(x, y)) return;
	if (has_been_visited(visited, x, y)) return;

	struct Position new_pos = { x, y, moves };
	enqueue(q, &new_pos);
}

bool evaluate_next_position(struct CircularQueue* q, struct List* visited) {
	if (queue_is_empty(q)) return true;

	struct Position next;
	dequeue(q, &next);
	// Multiple of the same position can be enqueued, make sure w're not counting duplicates
	if (has_been_visited(visited, next.x, next.y)) return false;

	int xl = next.x - 1, xr = next.x + 1;
	int yu = next.y - 1, yd = next.y + 1;

	if (next.moves < 50) {
		enqueue_neighbour(q, visited, xl, next.y, next.moves + 1);
		enqueue_neighbour(q, visited, xr, next.y, next.moves + 1);
		enqueue_neighbour(q, visited, next.x, yu, next.moves + 1);
		enqueue_neighbour(q, visited, next.x, yd, next.moves + 1);
	}

	append(visited, &next);
	return false;
}

int main(int argc, char** argv) {
	struct List* visited = new_list(4096, sizeof(struct Position)); 
	if (!visited) {
		printf("Failed to create visited list\n");
		return 1;
	}

	struct CircularQueue* q = new_queue(4096, sizeof(struct Position));
	if (!q) {
		printf("Failed to create queue\n");
		return 1;
	}

	struct Position initial = { START_X, START_Y, 0 };
	enqueue(q, &initial);

	while (!evaluate_next_position(q, visited)) ;
	printf("%d visited\n", visited->len);

	free_queue(q);
	free_list(visited);
	return 0;
}
