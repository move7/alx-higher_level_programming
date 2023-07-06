#!/usr/bin/python3
import sys


def is_safe(board, r, c):
    for i in range(r):
        if board[i] == c or board[i] - c == i - r or board[i] - c == r - i:
            return False
    return True


def solve_nqueens(N):
    board = [-1] * N
    solutions = []

    def backtrack(r):
        if r == N:
            solutions.append(board[:])
        else:
            for c in range(N):
                if is_safe(board, r, c):
                    board[r] = c
                    backtrack(r + 1)
                    board[r] = -1

    backtrack(0)

    for solution in solutions:
        print([[i, solution[i]] for i in range(N)])


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    N = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

if N < 4:
    print("N must be at least 4")
    sys.exit(1)

solve_nqueens(N)
