# import module
import sys
""" Output a single line containing the number of different possible Jack-O’-Lantern designs.
    The input consists of one line which contains three integers. The first, , indicates the
    number of eye designs. The second, , indicates the number of nose designs. The third, ,
    indicates the number of mouth designs. All three values are in the range [1, 500].
"""
#taking three integers as input
N, T, M = map(int, sys.stdin.readline().split())

# calculate the total number of diffrent possible Jack-O’-Lantern designs

total_designs = N * T * M
print(total_designs)
