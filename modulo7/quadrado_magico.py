import numpy as np

length = int(input())
matrix = []
for i in range(length):    
    matrix.append(input().strip().split(" "))

matrix = np.array(matrix, dtype=int)
magic_number = sum(matrix[0])


def check_rows(matrix, magic_number):
    return all(x == magic_number for x in np.sum(matrix, axis=1))


def check_columns(matrix, magic_number):
    return all(x == magic_number for x in np.sum(matrix, axis=0))


def check_main_diagonal(matrix, magic_number):
    return sum(np.diagonal(matrix)) == magic_number


def check_anti_diagonal(matrix, magic_number):
    return sum(np.fliplr(matrix).diagonal()) == magic_number


def magic_square(matrix, magic_number):
    return (check_rows(matrix, magic_number) and
            check_columns(matrix, magic_number) and
            check_main_diagonal(matrix, magic_number) and
            check_anti_diagonal(matrix, magic_number))


print(magic_square(matrix, magic_number))
