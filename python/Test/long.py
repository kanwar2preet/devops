#functions are reusable piece of code in a software
def say_hello():
    #block of functions
    print("Hello world")
#End of functions


say_hello()



########################################################
#function_param.py
def print_max(a, b):
    if a > b:
        print(a, 'is greater ')
    elif b > a:
        print(b, 'is greater')
    else:
        print('both are greater')



# passing literal values directly to function_param

print_max(5, 6)

x=8
y=4

print_max(x, y)
######################################################
#define a function to use a local variable
#gives a little example for defining scope of a variable

a=5
b=6
def adding_numbers():
    print(a+b)

adding_numbers()
print(a)


###############################################################
####global statement is used to declare variable ouside the scope of the function_param
###function_global.py
