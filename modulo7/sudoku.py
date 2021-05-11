import numpy as np


def is_sudoku(matrix):
    matrix = np.array(matrix)
    for i in range(9):
        if (len(set(matrix[:9, i])) != 9 or len(set(matrix[i, :9])) != 9):
            return "NAO"

    for i in range(0, 6, 3):
        for j in range(0, 6, 3):
            if (len(set(matrix[i:i+3, j:j+3].flatten())) != 9):
                return "NAO"
    return "SIM"


length = int(input())
for i in range(length):
    sudoku = []
    for _ in range(9):
        sudoku.append([int(w) for w in input().strip().split(" ")])

    print(f'Instacia {i+1}')
    print(is_sudoku(sudoku))
    print()
