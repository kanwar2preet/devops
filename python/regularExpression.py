import re

def Find(pattern,text):
    match = re.search(pattern,text)
    if match:
        print( match.group())
    else:
        print( 'not found')


# regular expression funtion defined above

Find('ig', 'called ig' )
