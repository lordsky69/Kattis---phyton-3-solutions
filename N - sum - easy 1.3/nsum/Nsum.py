# read input
# the number of integers to be added
n = int(input())
#the next line input as a string
numbers_list = input()
#the input splited 
numbers_to_add = numbers_list.split()

# convert each item to int type
for i in range(n):
    # convert each item to int type
    numbers_to_add[i] = int(numbers_to_add[i])

# Calculating the sum of list elements
print(sum(numbers_to_add))