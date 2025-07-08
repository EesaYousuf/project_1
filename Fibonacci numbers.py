def fibonacci(limit):
    a, b = 0, 1
    for _ in range(limit):
        yield a
        a, b = b, a + b
     # Usage
for num in fibonacci(7):
    print(num)  # Output: 0, 1, 1, 2, 3, 5, 8   