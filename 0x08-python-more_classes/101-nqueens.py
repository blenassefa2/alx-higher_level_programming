#!/usr/bin/python3
import sys
""" This module solves the n-queens problem"""


def calcpos(N):
    """
    calculates all valid positions valid for first row

    Args:
        N : int
            the current index
    Return:
        an empty string for invalid position
        the rest of queens position
    """
    final = []
    ans = []
    p_diag = set()
    n_diag = set()
    col = set()

    def backtracking(j):
        """
        recursively backtrack

        Args:
            j : row
        Return:
            nothing
        """
        if j == N:
            print(ans)
            return
        for c in range(N):
            if c in col or j + c in p_diag or j - c in n_diag:
                continue

            col.add(c)
            p_diag.add(j + c)
            n_diag.add(j - c)
            ans.append([j, c])

            backtracking(j + 1)

            col.remove(c)
            p_diag.remove(j + c)
            n_diag.remove(j - c)
            ans.pop()

    backtracking(0)
    return final


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    exit(1)

N = int(sys.argv[1])
if not isinstance(N, int):
    print("N must be a number")
    exit(1)
n = int(N)
if N < 4:
    print("N must be at least 4")
    exit(1)
a = calcpos(n)
