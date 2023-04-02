import os

os.chdir(r'C:\\Users\\lupiv\\Desktop\\Code\\Practice\\Python\\f9')

file1='copy.txt'
file2='log.txt'

with open(file1) as f:
    data1=f.read()

with open(file2) as f:
    data2=f.read()

if(data1==data2):
    print("Files are identical")
else:
    print('files are not identical')
