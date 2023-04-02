#other methods to read the file
import os

os.chdir(r'C:\\Users\\lupiv\\Desktop\\Code\\Practice\\Python\\f9')
f = open('sample1.txt','r')

data=f.readline() #read first line of file
print(data)

data=f.readline() #if we use it again then it will read 2nd line and so on
print(data)

f.close()