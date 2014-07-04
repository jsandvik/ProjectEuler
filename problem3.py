"""
    solution to problem 3
"""

def is_prime(number):
    """
        returns true/false if number is a prime number
    """
    for i in range(2, number):
        if number % i == 0:
            return False

    return True

def find_largest_prime_factor(number):
    """
        Returns largest prime factor
    """
    upper_bound = int(number ** 0.5)

    for i in range(upper_bound, 2, -1):
        if number % i == 0 and is_prime(i):
            return i

if __name__ == "__main__":
    prime = find_largest_prime_factor(600851475143)
    print "Largest Prime Factor: {0}".format(prime)
