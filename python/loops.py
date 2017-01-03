#Looping in python

#A:Print numbers in a list (using for loop)
for n in [2,4,5,6,7,8,]:
    print(n)
    

#A2 : for loop continued:
for n in range(8):
    print("numbers are",n)


#A3: for with range    
for n in range(3,5):
    print("ranges are",n)

#B1 : Whille loop
count = 0
while count <=5:
    print("going from 0 to 5,number is",count)
    count += 1
    
#Note : Break is used to exit loop & continue is used to skip the current block.

#C & D : Break and while:
count = 0
while count <= 10:
    print("trying to go to 10 starting from 0, current number is",count)
    count += 1
    if count >= 4:
        break
