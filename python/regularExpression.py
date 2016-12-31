# py to show the use of the regular expressions
import re

def Find(pattern,text):
    match = re.search(pattern,text)
    if match:
        print( match.group())
    else:
        print( 'not found')


# regular expression funtion defined above

Find('ig', 'called ig' )


# . (dot) for any character

Find ('..g','called piiii g much better: xyzg')
# searches from left to right and immediately stops when find the first one


#see below code if you want to search for a . character, basically put a \ to reduce specialness of dot character

Find (r'c\.','c.lled piiii g much better: xyzg')

#in above line r' tells to find something as it is and treats basically everything as raw


#to find a word character use \w like below

Find (r':\w\w\w','called piiii :cat much better: xyzg')

#to find the digits use \d like below
Find (r':\d\d\d','ca lled piiii g :123 better: xyzg')

#to find the whitespace use the /s

Find (r'\d\s\d\s\d\s','called piiii g 1 2 3 better: xyzg')
        
