"""
    solution to problem 4
"""

def is_palindromic_number(number):
    """
        Returns true if number is a 
        panlindromic number. False if not.
    """
    number_string = str(number)
    reverse_string = number_string[::-1]
    return number_string == reverse_string

if __name__ == "__main__":
    max_result = 0
    for i in range(999):
        for j in range(999):
            product = i * j
            if is_palindromic_number(product) and product > max_result:
                max_result = product

    print "Result: ", max_result