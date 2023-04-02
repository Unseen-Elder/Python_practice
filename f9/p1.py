import os

os.chdir(r'C:\\Users\\lupiv\\Desktop\\Code\\Practice\\Python\\f9')
# this is to specify the path of directory in which desired file is located

f = open('sample1.txt','r') #if we dont specify any mode then by default the mode is r
data = f.read()
#if i write f.read(5) then it will read first 5 characters of file
print(data)

f.close()