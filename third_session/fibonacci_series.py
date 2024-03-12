def fibonacci(n):
    fib_series = [0,1]
    for i in range(2, n):
        fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series[:n]

# test the function
n = 10
fib_series = fibonacci(n)
print(fib_series)