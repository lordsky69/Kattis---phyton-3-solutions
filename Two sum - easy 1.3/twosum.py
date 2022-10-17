# import module
import sys
""" Output a single integer, the sum of a + b.
    The input consists of a single line with two integers 0 <= a <= 1000 and 0 <= b <= 1000.
"""
#taking three integers as input
a, b = map(int, sys.stdin.readline().split())

# calculate the total number of diffrent possible Jack-O’-Lantern design
print((a + b))