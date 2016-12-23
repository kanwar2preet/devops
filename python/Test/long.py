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
