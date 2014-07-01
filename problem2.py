"""
    solution to problem 2
"""

UPPER_BOUND = 4000000

def find_sum():
    """
        Finds sum of even valued fibonacci terms up to the upper bound
    """
    term_1 = 1
    term_2 = 2
    total = 2
    while True:
        new_term = term_1 + term_2

        # Break if passing upper bound
        if new_term > UPPER_BOUND:
            break

        if new_term % 2:
            total += new_term

        term_1 = term_2
        term_2 = new_term

    print "Sum: {0}".format(total)

if __name__ == "__main__":
    find_sum()
