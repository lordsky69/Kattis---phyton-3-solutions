# import module
import sys
#taking two integers as input
base, height = map(int, sys.stdin.readline().split())

#print the area of triangle using formula (1/2)*height*base
print(0.5 * base * height)
