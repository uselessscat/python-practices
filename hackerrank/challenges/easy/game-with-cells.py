#!/bin/python3

# https://www.hackerrank.com/challenges/game-with-cells/problem

import math
import os
import random
import re
import sys


def game_with_cells(n, m):
    return ((n + 1) // 2) * ((m + 1) // 2)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = game_with_cells(n, m)

    fptr.write(str(result) + '\n')

    fptr.close()
