import os

os.chdir(r'C:\\Users\\lupiv\\Desktop\\Code\\Practice\\Python\\f9')

oldfile = 'sample1.txt'
newfile = 'Renamed_by_python.txt'

with open(oldfile) as f:
    content = f.read()

with open(newfile,'w') as f:
    f.write(content)

os.remove(oldfile)
