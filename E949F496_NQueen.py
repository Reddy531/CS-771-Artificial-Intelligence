
'''
CS 771 - Artificial Intelligence
Final Project Program
N-Queen Program using Python
Chakradhar Reddy Donuri
WSUID: E949F496
'''

import sys
import random
import itertools as it
import operator
from functools import lru_cache
from collections import Counter


def board_Start(board_size):
    def get_m(sol, row, col):
        return sum(queen_Attacks((r, c), (row, col))
                   for c, r in enumerate(sol, start=1))
    assign_b = []
    pool = set()
    whole = set(range(1, board_size + 1))
    n = 1
    while n < board_size:
        els = [(col, get_m(assign_b, col, n))
               for col in range(1, board_size + 1)]
        min_val = min(els, key=operator.itemgetter(1))[1]
        min_r = {el[0] for el in els if el[1] == min_val}
        min_r.difference_update(pool)
        if min_r:
            e = random.sample(min_r, 1)[0]
        else:
            els = whole - pool
            e = random.sample(els, 1)[0]
        assign_b.append(e)
        pool.add(e)
        n += 1
    last_e = (whole - pool).pop()
    assign_b.append(last_e)
    return assign_b


def display_Board(queen_positions):
    for i in range(len(queen_positions)):
        print("|", end="")
        for j in range(len(queen_positions)):
            if queen_positions[j] == i + 1:
                print(" x ", end="")
            else:
                print(" o ", end="")
            print("|", end="")
        print()


def queen_Attacks(position_1, position_2):
    return (position_1[0] == position_2[0] or
            position_1[1] == position_2[1] or
            abs(position_1[0] - position_2[0]) == abs(position_1[1] - position_2[1]))


def search_conf(sol, board_size, last):
    def true_conf(x):
        r = sol[x - 1]
        return any(x != col_1 and queen_Attacks((r, x), (row_1, col_1))
                   for col_1, row_1 in enumerate(sol, start=1))

    pool = list(range(1, board_size + 1))
    if last is not None:
        pool.remove(last)
    while pool:
        x = random.choice(pool)
        if true_conf(x):
            return x
        pool.remove(x)
    if last and true_conf(last):
        return last


def set_Val(sol, q, value):
    index = sol.index(value)
    sol[q - 1], sol[index] = value, sol[q - 1]


def conf_Count(sol, q):
    row = sol[q - 1]
    return sum(q != col_1 and queen_Attacks((row, q), (row_1, col_1))
               for col_1, row_1 in enumerate(sol, start=1))


def minimum_conflicts(board_size, max_size=100000, start_state=[]):
    current = board_Start(board_size)
    last = None
    p = range(max_size) if max_size > 0 else it.count()
    for it_count in p:
        q = search_conf(current, board_size, last)
        last = q
        if q is None:
            return current, it_count
        val = choose_Val(q, current, board_size)
        set_Val(current, q, val)
    return None, max_size


def choose_Val(q, current, board_size):
    c_Vector = []
    current_Op = current[:]
    for val in range(1, board_size + 1):
        set_Val(current_Op, q, val)
        c_Vector.append(conf_Count(current_Op, q))
        current_Op = current[:]
    min_c = min(c_Vector)
    return random.choice([i for (i, v) in enumerate(c_Vector, start=1)
                          if v == min_c])


def main(board_size, start_state):
    board_Solution, i = minimum_conflicts(board_size, -1, start_state)
    if board_Solution:
        print("")
        print("-----------------OUTPUT---------------------")
        display_Board(board_Solution)

    else:
        print("Timeout")


if __name__ == "__main__":
    n = int(input('Enter Size of the Board i.e. n>=4: '))
    print("*******Queen Position index start from 0********")
    input_array = []
    Matrix = [[0 for x in range(n)] for y in range(n)]
    if(n >= 4):
        for i in range(n):
            print("Enter the Queen position in column - ", i+1, " :")
            row_value = int(input())
            input_array.append(row_value)
            for j in range(n):
                if(row_value < n):
                    if(j == row_value):
                        Matrix[i][j] = "x"
                    else:
                        Matrix[i][j] = "o"
                else:
                    print("----Index Exceeds!----")
                    break
            print("")

        if(len(input_array) == n):
            print("")
            if(max(input_array) < n):
                print(
                    'Initial Start State of Queen positions in each column on the Board: ', input_array)
                print("")
                print("----------------START STATE----------------------")
                t_matrix = zip(*Matrix)
                for row in t_matrix:
                    print(row)
                main(n, input_array)
    else:
        print("")
        print('Please enter the input value n greater than or equal to 4')
