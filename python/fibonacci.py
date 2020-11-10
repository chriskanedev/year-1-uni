length = 10

def fibonacci(n):
    if n == 0:  # 0 is the first Fibonacci number
        return 0
    elif n==1:  # 1 is the second Fibonacci number
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)


# Main
for i in range(0, length):
    print("{0} ",fibonacci(i))
