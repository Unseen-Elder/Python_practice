import os

os.chdir(r'C:\\Users\\lupiv\\Desktop\\Code\\Practice\\Python\\f9\\tables')

for i in range(1,21):
    f=open(f"table{i}.txt",'w')
    for j in range(1,11):
        f.write(f'{i} X {j} = {i*j}')
        if(j != 10):
            f.write('\n')
    f.close()