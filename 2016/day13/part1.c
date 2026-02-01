#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <limits.h>
#include "../utils/list.h"

#define START_X 1
#define START_Y 1
#define GOAL_X 31
#define GOAL_Y 39

struct Position {
	int x, y, moves;
	bool open;
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
	return x > 0 && y > 0 && !is_wall(x, y);
}

int distance_to_goal(struct Position* pos) {
	int dx = abs(GOAL_X - pos->x);
	int dy = abs(GOAL_Y - pos->y);
	return (dx * dx) + (dy * dy);
}

struct Position* get_closest_position(struct List* l) {
	struct Position* closest_pos, *current_pos;
	int shortest_dist = INT_MAX;
	for (int i = 0; i < l->len; ++i) {
		get_at(l, i, &current_pos);
		if (!current_pos->open) continue;
		int dist = distance_to_goal(current_pos);
		if (dist < shortest_dist) {
			shortest_dist = dist;
			closest_pos = current_pos; 
		}
	}

	return closest_pos;
}

struct Position* position_with_xy(struct List* positions, const int x, const int y) {
	struct Position* pos;
	for (int i = 0; i < positions->len; ++i) {
		get_at(positions, i, &pos);
		if (pos->x == x && pos->y == y) return pos;
	}
	return NULL;
}

void add_position_to_list(struct List* positions, int x, int y, int moves) {
	if (!is_valid_space(x, y)) {
		return;
	}

	struct Position* existing = position_with_xy(positions, x, y);
	if (existing != NULL) {
		return;
	}

	struct Position* p = malloc(sizeof(struct Position));
	if (!p) {
		printf("Error allocating position");
		return;
	}

	p->x = x; p->y = y; p->moves = moves; p->open = true;
	append(positions, &p);
}

bool evaluate_next_position(struct List* l) {
	struct Position* pos = get_closest_position(l);
	if (pos->x == GOAL_X && pos->y == GOAL_Y) {
		printf("Reached the goal in %d moves\n", pos->moves);
		return true;
	}

	printf("Evaluating position (%d, %d)\n", pos->x, pos->y);

	int xl = pos->x - 1, xr = pos->x + 1;
	int yu = pos->y - 1, yd = pos->y + 1;

	add_position_to_list(l, xl, pos->y, pos->moves + 1);
	add_position_to_list(l, xr, pos->y, pos->moves + 1);
	add_position_to_list(l, pos->x, yu, pos->moves + 1);
	add_position_to_list(l, pos->x, yd, pos->moves + 1);

	pos->open = false;

	return false;
}

void print_map(struct List* positions) {
	for (int i = 0; i < 50; ++i) {
		for (int j = 0; j < 50; ++j) {
			if (is_wall(j, i))
				printf("X");
			else {
				struct Position* pos = position_with_xy(positions, j, i);
				if (pos == NULL)
					printf(" ");
				else
					printf("O");
			}
		}
		printf("\n");
	}
}

int main(int argc, char** argv) {
	struct List* positions = new_list(1000, sizeof(struct Position*)); 
	if (!positions) {
		printf("List creation failed!\n");
		return 0;
	}

	struct Position* initial = malloc(sizeof(struct Position));
	initial->x = START_X; initial->y = START_Y; initial->moves = 0; initial->open = true;
	append(positions, &initial);
	print_map(positions);
	while (!evaluate_next_position(positions)) {
		print_map(positions);
		getchar();
	}

	struct Position* pos;
	for (int i = 0; i < positions->len; ++i) {
		get_at(positions, i, &pos);
		free(pos);
	}

	free_list(positions);
	return 0;
}
