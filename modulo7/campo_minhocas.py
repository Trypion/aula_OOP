import numpy as np

rows, columns = input().strip().split(" ")

matrix = []

for _ in range(int(rows)):
    matrix.append([int(w) for w in input().strip().split(" ")])


def find_biggest_number(matrix):
    row = max(np.sum(matrix, axis=1))
    column = max(np.sum(matrix, axis=0))
    return max(row, column)


print(find_biggest_number(matrix))
