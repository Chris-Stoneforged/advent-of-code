#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "../utils/circular_queue.h"
#include "../utils/list.h"

#define FLOORS 4
#define ELEMENTS 10

#define POG 1 << 0
#define POM 1 << 1
#define THG 1 << 2
#define THM 1 << 3
#define PRG 1 << 4
#define PRM 1 << 5
#define RUG 1 << 6
#define RUM 1 << 7
#define COG 1 << 8
#define COM 1 << 9

struct State {
	struct State* parent;
	unsigned int moves;
	unsigned int current_floor;
	unsigned int floors[FLOORS];
};

bool fhm(int f, int m) {
	return (f & m) == m;
}

bool fhog(int f, int g) {
	return (
		(g != POG && (f & POG) == POG) ||
		(g != THG && (f & THG) == THG) ||
		(g != PRG && (f & PRG) == PRG) ||
		(g != RUG && (f & RUG) == RUG) ||
		(g != COG && (f & COG) == COG)) &&
		(f & g) == 0;
}

bool is_floor_valid(int f) {
	if (
		(fhm(f, POM) && fhog(f, POG)) ||
		(fhm(f, THM) && fhog(f, THG)) ||
		(fhm(f, PRM) && fhog(f, PRG)) ||
		(fhm(f, RUM) && fhog(f, RUG)) ||
		(fhm(f, COM) && fhog(f, COG))
		) {
		return false;
	}
	return true;
}

bool states_are_equal(struct State* a, struct State* b) {
	for (int i = 0; i < FLOORS; ++i){
		if (a->floors[i] != b->floors[i])
			return false;
	}
	if (a->current_floor != b->current_floor)
		return false;

	return true;
}

bool has_state_been_done(struct State* s) {
	struct State* p = s->parent;
	while (p != NULL) {
		if (states_are_equal(p, s))
			return true;
		p = p->parent;
	}
	return false;
}

bool evaluate_move(int f, int d, int move, int* fn, int* dn) {
	if ((f & move) != move) return false;
	*fn = f & ~move;
	*dn = d | move;
	return is_floor_valid(*fn) && is_floor_valid(*dn);
}

void print_state(struct State* s) {
	char* names[ELEMENTS] = { "POG", "POM", "THG", "THM", "PRG", "PRM", "RUG", "RUM", "COG", "COM" };
	int f, m;
	for (int i = FLOORS - 1; i >= 0; --i) {
		f = s->floors[i];
		printf("F%d %c", i + 1, i == s->current_floor ? 'E' : '.');
		for (int j = 0; j < ELEMENTS; ++j) {
			m = 1 << j;
			printf(" %s ", (f & m) == m ? names[j] : " . ");
		}
		printf("\n");
	}
	printf("Moves: %d\n", s->moves);
}

void handle_move(struct CircularQueue* q, struct State* s, int i, int m) {
	int fn, dn;
	int c = s->current_floor;
	int f = s->floors[c];
	int d = s->floors[i];

	if (evaluate_move(f, d, m, &fn, &dn)) {
		struct State* n = malloc(sizeof(struct State));
		memcpy(n, s, sizeof(struct State));
		n->floors[c] = fn;
		n->floors[i] = dn;
		n->current_floor = i;
		n->parent = s;
		++n->moves;

		if (!has_state_been_done(n)) {
			enqueue(q, &n);
		}
		else {
			free(n);
		}
	}
}

int main(int argc, char** argv) {
	unsigned int max = POG | POM | THG | THM | PRG | PRM | RUG | RUM | COG | COM;
	int initial_floors[4] = {
		POG | THG | THM | PRG | RUG | RUM | COG | COM,
		POM | PRM,
		0,
		0
	};

	struct List* l = new_list(1000000000, sizeof(struct State*));
	struct CircularQueue* q = new_queue(1000000000, sizeof(struct State*));
	struct State* s = malloc(sizeof(struct State));
	s->moves = 0;
	s->parent = NULL;
	s->current_floor = 0;
	memcpy(s->floors, &initial_floors, sizeof(int) * 4);

	enqueue(q, &s);
	for (;;) {
		if (!dequeue(q, &s)) goto end;
		if (s->floors[FLOORS - 1] == max) {
			printf("All items on the fourth floor in %d moves\n", s->moves);
			break;
		}
		int c = s->current_floor;
		for (int i = c - 1; i <= c + 1; ++i) {
			if (i < 0 || i >= FLOORS || i == c) continue;
			for (int j = 0; j < ELEMENTS; ++j) {
				handle_move(q, s, i, 1 << j);
				for (int k = j + 1; k < ELEMENTS; ++k)
					handle_move(q, s, i, (1 << j) | (1 << k));
			}
		}
		append(l, &s);
	}

	while (!queue_is_empty(q)) {
		dequeue(q, &s);
		free(s);
	}

	for (int i = 0; i < l->len; ++i) {
		get_at(l, 0, &s);
		free(s);
	}

end:
	free_list(l);
	free_queue(q);
	return 0;
}
