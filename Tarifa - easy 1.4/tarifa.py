# import module
import sys

# read input
# monthly internet plan value
x = int(sys.stdin.readline())

# the number of months that Pero used the internet
n = int(sys.stdin.readline())

# total Mb available in first n months
available = x * n

# total Mb used in n moths
spent = 0
for i in range(n):
    spent += int(sys.stdin.readline())
    
# available Mb to be used in n+1 month
print(available - spent + x)
    
