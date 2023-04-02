import os
import random

os.chdir(r'C:\\Users\\lupiv\\Desktop\\Code\\Practice\\Python\\f9')

def score():
    return random.randint(0,100)

f=open("highscore.txt",'r')
a=score()
data=f.read()
f.close()
if(data==''):
    f=open("highscore.txt",'w')
    f.write(str(a))
    f.close()
elif(a>int(data)):
    f=open("highscore.txt",'w')
    f.write(str(a))
    f.close()
else:
    pass


with open('highscore.txt','r') as f:
    data=f.read()

print(data)