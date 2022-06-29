#!/usr/bin/python3
import sys
""" This module solves the n-queens problem"""

if len(sys.argv) != 2:
    print("Usage: nqueens N")
    exit(1)

N = int(sys.argv[1])

#check if input is valid
if not isinstance(N, int):
    print("N must be a number")
    exit(1)
if N < 4:
    print("N must be at least 4")
    exit(1)


#imlement the check function
def calcpos():
    """ 
    calculates all valid positions valid for first row

    Args:
        x : int
            the current index
    Return:
        an empty string for invalid position
        the rest of queens position 
    """
    final = []
    ans = []
    #build the diagonals and the columns dictionary
    p_diag = set() 
    n_diag = set()

    col = set()

    def backtracking(j):
        if j == N:
            print(ans)
            final.append(ans)
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
calcpos()

