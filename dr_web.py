def fibonacci(num=4):
    fib1, fib2 = 1, 0
    for _ in range(num):
        print(fib2, end=' ')
        fib1, fib2 = fib1 + 2*fib2, 2*fib1 + 3*fib2
fibonacci(4)
