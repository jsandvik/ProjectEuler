"""
    solution to problem 1
"""

UPPER_BOUND = 1000

def find_sum():
    """
        Finds sum of all multiples of 3 and 5 below the upper bound
    """
    total = 0
    for i in range(1, UPPER_BOUND):
        if (i % 3 == 0) or (i % 5 == 0):
            total += i

    print "Sum: {0}".format(total)

if __name__ == "__main__":
    find_sum()
