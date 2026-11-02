def fibonacci_recursive(n):
    """Recursive function to find the nth Fibonacci number."""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

def generate_fibonacci_series(terms):
    """User-defined function to generate the Fibonacci series up to 'terms'."""
    series = []
    for i in range(terms):
        series.append(fibonacci_recursive(i))
    return series

if __name__ == "__main__":
    try:
        num_terms = int(input("Enter the number of terms for the Fibonacci series: "))
        if num_terms <= 0:
            print("Please enter a positive integer.")
        else:
            fib_series = generate_fibonacci_series(num_terms)
            print(f"Fibonacci series up to {num_terms} terms: {fib_series}")
    except ValueError:
        print("Please enter a valid integer.")