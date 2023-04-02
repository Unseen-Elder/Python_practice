import os

os.chdir(r'C:\\Users\\lupiv\\Desktop\\Code\\Practice\\Python\\f9')

f=open('poem.txt','r')
data = f.read()
word = input("Entre the word you want to search in File : ")
a=data.find(word)
if(a!=-1):
    print("Yes")
else:
    print("No")

f.close()