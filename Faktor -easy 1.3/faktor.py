# import module
import sys
""" Output the minimal number of scientists you need to bribe.
    First and only line of input will contain 2 integers, A (1 <= A <= 100), 
    the number of articles you plan to publish and I (1 <= I <= 100)), 
    the impact factor the owners require.
"""
#taking two integers as input, the number of articles and the impact factor
A, I = map(int, sys.stdin.readline().split())

# calculate the minimal number of scientists you need to bribe
min_scientists = A * (I - 1) + 1
print(min_scientists)
