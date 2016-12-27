import time as t
from os import path

def createFile(dest):
    '''
    Script creates a file at the passed in location
    with names file based on date
    '''

    date = t.localtime(t,time())

    ##FileName =Month_Day_Year
    name = '%d_%d_%d.txt'%(date[1],date[2],(date[0]%100))

    if not(path.isfile(dest+name)):
        f= open(dest+name,'w')
        f.write('\n'*30)
        f.close()

if __name__ =='__main__':
    destination = "/tmp"
    createFile(destination)
    raw_input("done")



