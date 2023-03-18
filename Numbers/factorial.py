# Factorial Finder
# The Factorial of a positive integer, n, is defined as the product of the
# sequence n, n-1, n-2, ...1 and the factorial of zero, 0, is defined as
# being 1. Solve this using both loops and recursion.

def fact_loop(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact


def fact_rec(n):
    if n == 0:
        return 1
    else:
        return n * fact_rec(n - 1)
