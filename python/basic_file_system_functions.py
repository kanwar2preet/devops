import os
os.getcwd() #getting pwd
os.listdir() # ls 
os.listdir("/var/log")   #ls /var/log
os.mkdir("jest")
os.listdir()
os.chdir("jest")
os.getcwd()
os.chdir("/home/kanwar")
#os.walk can walk down directory paths
for dirpath,dirnames,filenames in os.walk(os.getcwd(),topdown="true"):
    print(dirpath,filenames)
    
    
#continuing
    
