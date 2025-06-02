class Fibonacci:
    def __init__(self, n):
        self.n = n

    def series(self):
        result = []
        a, b = 0, 1
        for _ in range(self.n):
            result.append(a)
            a, b = b, a + b
        return result

# Example usage:
# fib = Fibonacci(10)
# print(fib.series())
