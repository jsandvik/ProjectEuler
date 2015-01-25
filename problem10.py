"""
    Solution to problem 10
"""

def isprime(x):
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    else:
        return True

primes = [i for i in range(2, 2000001) if isprime(i)]
prime_sum = reduce(lambda x, y: x + y, primes)
print "Prime sum: ", prime_sum
