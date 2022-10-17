# import module
import sys
""" Output one line per test case, with the maximum number of appliances that can be powered.
"""
#taking three integers as input
test_cases = int(input())
outlets = 0

for i in range(test_cases):
    # the list contained the number of strips and the outlets of each strip
    list_strips = list(map(int, sys.stdin.readline().split()))
    total_outlets = sum(list_strips[1:])
    # calculate the total number of available outlets( substract the occcupied outlets which will connect each other) 
    outlets = total_outlets - int(list_strips[0]-1)
    print(outlets)