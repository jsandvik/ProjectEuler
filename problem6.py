"""
    solution to problem 6
"""

if __name__ == "__main__":
    square_of_sum = sum(range(1, 101)) ** 2
    sum_of_squares = sum([x**2 for x in range(1, 101)])
    print square_of_sum - sum_of_squares