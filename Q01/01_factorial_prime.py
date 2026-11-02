def calculate_factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    try:
        number = int(input("Enter an integer: "))
        
        # Factorial calculation using loops
        fact = calculate_factorial(number)
        print(f"Factorial of {number}: {fact}")
        
        # Prime check using conditional and looping constructs
        if number > 0:
            prime_status = is_prime(number)
            if prime_status:
                print(f"{number} is a prime number.")
            else:
                print(f"{number} is not a prime number.")
        else:
            print(f"{number} is not a positive integer, so primality is not applicable.")
            
    except ValueError:
        print("Please enter a valid integer.")