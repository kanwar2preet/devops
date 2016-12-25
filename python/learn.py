#check git ssh auth
# This is the start of the python script for learning python and act as a document backup
#! python
# measure the length of the strings
a= ['vinty','gamesarethere','awesome']
for x in a:
    print x, len(x)

##############################################################
##Learning default Agruments in funtions

def function(message,times=1):
    print(message * times)

function('hello')
function('hello', 8)
##############################################
####Keyword Arguments
def key_arguments(a=4, b=6, c=9):
    print('a is',a, 'b is', b, 'c is',c)

key_arguments(2,4)
key_arguments(1,3)
key_arguments(1,1,1)
###########################################
###############return statement

def maximum(x,y):
    if x > y:
        return x
    elif  x == y:
        return "numbers are equal"
    else:
        return y

print(maximum(2,3))
    

######################################################
##############Doc strings
def print_max(x,y):
    '''Prints the maximum of two numbers.

    The two values must be integers.'''
    x=int(x)
    y=int(y)

    if x > y:
        print('x is greater')
    else:
        print('y is greater')

print_max(3,5)
print(print_max.__doc__)

######################################################

    
    
    
    
    
    

