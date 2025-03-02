def is_prime(n):
    if n < 2:
        return False  # Numbers less than 2 are not prime
    for i in range(2, n):  # Check divisibility from 2 to n-1
        if n % i == 0:
            return False  # Found a factor, so not prime
    return True  # No factors found, so it's prime

print(is_prime(64))