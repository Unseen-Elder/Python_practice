#impt tip, once you read full file , you have to open it again to read again

import os

os.chdir(r'C:\\Users\\lupiv\\Desktop\\Code\\Practice\\Python\\f9')

list_1=[]
list_2=[]
a = 0
i=0
text=True

with open('log.txt','r') as f:
    while(text):
        i =i+1
        text=f.readline()
        b=text.find('WARNING')
        if(b!=-1):
            list_1.append(i)
        else:
            pass

f=open('log.txt','r')
data=f.read()
f.close()

while(a != -1) :
    
    a=data.find('WARNING')
    if(a!=-1):
        list_2.append(str(a))
    
    for i in range(a,a+7):
        list_3 = list(data)
        list_3[i]='#'
        data=''.join(list_3)

print(list_1,len(list_1))
print(list_2,len(list_2))