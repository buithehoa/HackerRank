#!/bin/python3

import sys

def input_matrix():
    matrix = [ [ 0 for i in range(MATRIX_SIZE) ] for j in range(MATRIX_SIZE) ]

    for i in range(MATRIX_SIZE):
        row = input().strip().split(' ')
        for j in range(MATRIX_SIZE):
            matrix[i][j] = int(row[j])

    return matrix

def max_hourglass_sum(matrix):
    HOURGLASSES_PER_ROW = MATRIX_SIZE - 2
    HOURGLASS_SIZE = 3

    max_hourglass_sum = -1 * sys.maxsize

    for i in range(HOURGLASSES_PER_ROW):
        for j in range(HOURGLASSES_PER_ROW):
            hourglass_sum = 0
            for g in range(i, i + HOURGLASS_SIZE):
                for h in range (j, j + HOURGLASS_SIZE):
                    if g == i or g == (i + HOURGLASS_SIZE - 1) or ((g == i + 1) and (h == j + 1)):
                        hourglass_sum += matrix[g][h]

            if hourglass_sum > max_hourglass_sum: max_hourglass_sum = hourglass_sum

    return max_hourglass_sum

if __name__ == "__main__":
    MATRIX_SIZE = 6
    matrix = input_matrix()
    print(max_hourglass_sum(matrix))
