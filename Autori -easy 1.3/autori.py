# import module
import sys
"""Transform the long variatons into short variatiions of diffrent scientific great names.
E.g:Scientific papers reference earlier works a lot and it’s not uncommon for one document to use 
two different naming conventions: the short variation (e.g. KMP) using only the first letters of authors 
last names and the long variation (e.g. Knuth-Morris-Pratt) using complete last names separated by hyphens.
The first and only line of input will contain at most  characters, uppercase and lowercase letters of the 
English alphabet and hyphen (‘-’ ASCII ). The first character will always be an uppercase letter. Hyphens 
will always be followed by an uppercase letter. All other characters will be lowercase letters.
"""
# read input
input = sys.stdin.readline()
#printing the first letter of each word from the the long string  
short_version = ''.join([input[:1] for input in input.split('-')])
print(short_version)