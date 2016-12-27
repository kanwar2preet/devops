print("Hello")

print("Concatenation of strings")

print('Alice' + 'bob')


##Learning default Agruments in funtions
#Python's default arguments are evaluated once when the function is defined, not each time the function is called.


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

##############################################

