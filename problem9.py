"""
    solution to problem 9
"""

for a in range(1, 333):
    for b in range(a+1, (1000 - a) // 2):
        c = 1000 - a - b
        if a**2 + b**2 == c**2:
            print "Pythagorean triplet: "
            print "a: ", a
            print "b: ", b
            print "c ", c
            print "abc: ", a*b*c
