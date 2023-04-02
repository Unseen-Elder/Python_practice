import os

os.chdir(r'C:\\Users\\lupiv\\Desktop\\Code\\Practice\\Python\\f9')

with open('poem.txt','r') as f:
    data=f.read()

with open('copy.txt','w') as f:
    f.write(data)