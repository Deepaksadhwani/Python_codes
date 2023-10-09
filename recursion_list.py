n = 5

def reverse_count(n):
    if n == 0:
        return
    print(n, end=" ")
    return reverse_count(n-1)
    #output: 5 4 3 2 1
def count(n):
    if n == 0:
        return
    count(n-1)
    print(n,end=" ")
    #output: 1 2 3 4 5

def sum_n(n):
    if n == 1:
        return 1
    return n + sum_n(n-1)
    # output: 15 (5+4+3+2+1)

def factorial_n(n):
    if n == 1:
        return 1
    return n * factorial_n(n-1)
    # output: 15 (5*4*3*2*1)
def fibonacci_n(n):
    if n == 0 or n == 1:
        return n
    return fibonacci_n(n-1) + fibonacci_n(n-2)
    # output: 5 (0,1,1,2,3) example: (n - 1 = 3) + (n -2 = 2)) 
    # if testcase n  = 6, output: 8 (0, 1, 1, 2, 3,5) example ((n - 1 = 5) + (n -2 = 3))
