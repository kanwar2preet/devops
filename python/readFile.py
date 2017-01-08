print("tutorial to read files in python")
#open a file in a read mode, print its name
f = open('test.txt','r')
print("opening text file in",f.mode,"mode", )
print("Name of the file is",f.name)
#always close a file after reading it
f.close
print("###################Another_Method to view contents of file#####################################")
#print("above method is used rarely as it opens the file and we have to close it manually,lets look at another way to do it")
with open('test.txt','r') as f:
	f_contents = f.read()
	print(f_contents)
	#above code will open and close the file after exiting the block

#If we use f.readlines, it will print lines in form of list
#f.readline() will print one line at a time
#print statement in general puts a newwline at the end of the file.


#with f.read, we can specify the amount of data to read so that we donot end up with 
#any memory issue
