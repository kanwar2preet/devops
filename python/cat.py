#! /usr/local/bin/python3
print("/n/n this program acts as a cat utility, it will read the file and print it line by line")
import sys


def Cat(filename):
	f = open(filename,'rU')
	for line in f:
		print(line,end='')
	f.close()	
		
 
# Define a main() function 
def main():
	Cat(sys.argv[1])	
	
	
#this  is the standard boilerplate that calls the main() function

if __name__ == '__main__':
	main()
		
