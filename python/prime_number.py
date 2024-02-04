"""
Prime Number Checker Function

Objective:
Write a function named 'is_prime' to determine whether a given number is a prime number.

Function Parameter:
number (integer): The number to be checked for primality.

Instructions:
- The function should return 'True' if the 'number' is a prime number and 'False' otherwise.
- A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
- Consider edge cases, such as when the input is less than 2, which is not a prime number.
- https://mathspar.com/prime-numbers/#how-to-tell-if-a-number-is-prime

Example Test Cases:
1. is_prime(11) should return 'True', as 11 is a prime number.
2. is_prime(4) should return 'False', as 4 is not a prime number.
3. is_prime(2) should return 'True', as 2 is a prime number.
4. is_prime(1) should return 'False', as 1 is not considered a prime number.
"""


def is_prime(number):
    # Implement the logic to determine if the number is prime
    # Return True if the number is prime, False otherwise
    # Check if the number is less than 2 (not a prime number)
    if number < 2:
        return False
    
    # Check for divisibility by numbers from 2 to the square root of the number
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False  # Number is divisible by i, not a prime number
    
    return True  # If no divisors found, the number is prime
    pass  # Delete this after implementing some code inside this function


# Test cases
print(is_prime(11))  # Expected output: True
print(is_prime(4))  # Expected output: False
print(is_prime(2))  # Expected output: True
print(is_prime(1))  # Expected output: False
