"""
    solution to problem 5
"""
from itertools import count

if __name__ == "__main__":
    for i in count(10, step=10):
        for j in range(2, 21):
            if i % j != 0:
                break
        else:
            print "Result: ", i
            break
