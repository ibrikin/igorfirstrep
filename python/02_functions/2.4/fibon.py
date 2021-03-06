def fibn(n):
    """
    Iterative method Fibonacci numbers
    """
    if n == 0: return n
    if n == 1: return n
    numFirst = 0
    numSecond = 1
    result = 1
    count = 1
    while count < n:
        result = numFirst + numSecond
        numFirst = numSecond 
        numSecond = result 
        count += 1
    return result

def fib(n):
    a,b = 0,1
    for i in range(n):
        a,b =b,a+b
    return a

x = fibn(10)
y = fib(10)
print(x, y)