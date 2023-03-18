# Fibonacci Sequence
# Enter a number and have the program generate the Fibonacci sequence to
# that number or to the Nth number.

def fib(n, *, mode='Nth'):
    match mode:
        case 'Nth':
            if n < 2:
                return n
            else:
                return fib(n - 1) + fib(n - 2)
        case 'All':
            fib_seq = []
            if n == 1 or n == 2:
                return 1
            else:
                for x in range(n):
                    print(fib(x), end=' ')
                return fib(n - 1) + fib(n - 2)


print(fib(7, mode='All'))
