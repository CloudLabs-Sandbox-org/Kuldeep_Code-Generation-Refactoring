class Fibonacci:
    """
    A class to generate the Fibonacci series up to n terms.
    """
    def __init__(self, n):
        if not isinstance(n, int) or n < 0:
            raise ValueError("n must be a non-negative integer")
        self.n = n

    def generate_series(self):
        """
        Generate the Fibonacci series up to n terms.
        Returns:
            list: A list containing the Fibonacci series.
        """
        result = []
        a, b = 0, 1
        for _ in range(self.n):
            result.append(a)
            a, b = b, a + b
        return result

# Example usage:
# fib = Fibonacci(10)
# print(fib.generate_series())
