#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define SCREEN_WIDTH 50
#define SCREEN_HEIGHT 6

void apply_rect(char *dimensions, int screen[SCREEN_HEIGHT][SCREEN_WIDTH]) {
	char *x_str = strtok(dimensions, "x"), *y_str = strtok(NULL, "x");
	int x = atoi(x_str), y = atoi(y_str);
	for (int i = 0; i < y; i++) {
		for (int j = 0; j < x; j++)
			screen[i][j] = 1;
	}
}

void apply_rotate_column(char *directions, int screen[SCREEN_HEIGHT][SCREEN_WIDTH]) {
	int tmp_col[SCREEN_HEIGHT];
	char *col_str = strtok(directions, "x= by"), *num_str = strtok(NULL, "x= by");
	int col = atoi(col_str), num = atoi(num_str);

	for (int i = 0; i < SCREEN_HEIGHT; i++) {
		tmp_col[i] = screen[i][col];
	}
	for (int i = 0; i < SCREEN_HEIGHT; i++) {
		screen[i][col] = tmp_col[(i + SCREEN_HEIGHT - num) % SCREEN_HEIGHT];
	}
}

void apply_rotate_row(char *directions, int screen[SCREEN_HEIGHT][SCREEN_WIDTH]) {
	int tmp_row[SCREEN_WIDTH];
	char *row_str = strtok(directions, "y= by"), *num_str = strtok(NULL, "y= by");
	int row = atoi(row_str), num = atoi(num_str);

	for (int i = 0; i < SCREEN_WIDTH; i++) {
		tmp_row[i] = screen[row][i];
	}
	for (int i = 0; i < SCREEN_WIDTH; i++) {
		screen[row][i] = tmp_row[(i + SCREEN_WIDTH - num) % SCREEN_WIDTH];
	}
}

int count_on(int screen[SCREEN_HEIGHT][SCREEN_WIDTH]) {
	int on = 0;
	for (int y = 0; y < SCREEN_HEIGHT; y++) {
		for (int x = 0; x < SCREEN_WIDTH; x++)
			on += screen[y][x];
	}
	return on;
}

int main(int argc, char** argv) {
	FILE* file = fopen(argv[1], "r");
	if (file == NULL) {
		perror("Failed to open file");
		return 1;
	}

	char *line = NULL;
	int screen[SCREEN_HEIGHT][SCREEN_WIDTH];
	char *delim = " \n";
	char *token;
	size_t len;
	ssize_t read;

	memset(screen, 0, sizeof(screen));
	
	while((read = getline(&line, &len, file)) != -1) {
		token = strtok(line, delim);
		if (strcmp(token, "rect") == 0) {
			apply_rect(strtok(NULL, delim), screen);
			continue;
		}

		// If first toke is not "rect", it will be rotate, so don't need to explicitly check
		token = strtok(NULL, delim);
		if (strcmp(token, "row") == 0) {
			apply_rotate_row(line + 11, screen);
		}
		else {
			apply_rotate_column(line + 14, screen);
		}
	}

	printf("%d\n", count_on(screen));

	free(line);
	fclose(file);
	return 0;
}
