"""
    solution to problem 6
"""
from math import sqrt
from itertools import count

def is_prime(number):
    for i in range(2, int(sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

if __name__ == "__main__":
    number_of_primes = 0
    for i in count(2):
        if is_prime(i):
            number_of_primes += 1
        if number_of_primes == 10001:
            print "Result: ", i
            break
