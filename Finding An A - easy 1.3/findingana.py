# import module
import sys

# read input
word = sys.stdin.readline()
#the index position of 'a' letter in the input
index = word.find('a')
#the substring
output =''
if index != -1:
    output = word[index:]
    
print(output)
    
