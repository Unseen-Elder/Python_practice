import os

os.chdir(r'C:\\Users\\lupiv\\Desktop\\Code\\Practice\\Python\\f9')

with open('sample2.txt','r') as file:
    data=file.read() #no need to open and close files again and again with this syntax

print(data)

with open('sample2.txt','a') as file:
    file.write('I am appending 4th line\n')

with open('sample2.txt','r') as file:
    data=file.read()

print(data)