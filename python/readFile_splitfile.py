import os
#below to check the current working directory
os.getcwd()
os.chdir('/home/home/home/home/python')
print(os.getcwd())
file = open('sketch.txt')
#by default data.readline puts a newline, so we use end='' 
print(file.readline(),end='')
#we if use printline again, next line will be read from file
print(file.readline(),end='')
# use seek to return to start of the file
file.seek(0)
print(file.readline(),end='')
file.seek(0)
for lines in file:
	print(lines,end='')

#close the file after using open with file
file.close()

print(end='')
print('Now lets the split function to split the data before and after')
print(os.getcwd())

one = open('sketch.txt')
for data_lines in one:
	if not data_lines.find(':') == -1:
		(role,line_spoken) = data_lines.split(':',1)
		print(role,end='')
		print(' said:',end='')
		print(line_spoken,end='')
