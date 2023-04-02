import os

os.chdir(r'C:\\Users\\lupiv\\Desktop\\Code\\Practice\\Python\\f9')

with open('Censor.txt') as f:
    data=f.read()

list=['Donkey','donkey','monkey','Monkey']

for item in list:
    a=data.find(item)
    if(a!=-1):
        data=data.replace(item,'#'*len(item))
    
    else:
        pass

with open('Censor.txt','w') as f:
    f.write(data)
