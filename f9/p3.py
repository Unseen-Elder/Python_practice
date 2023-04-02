import os

os.chdir(r'C:\\Users\\lupiv\\Desktop\\Code\\Practice\\Python\\f9')
f = open('sample2.txt','w') 

# r is for read, w is for write, a for append, + for update
# a will help to write at the end of file
# + will help to either read or write the file

#difference between w and a is that , when we use w then the file will become empty and it will be replaced by new text written to file
#but when we use append we can write at the end of file

f.write('I am writing\n')
f.write("This is 2nd line\n")
# whatever we write before closing file will be saved in file , but when we close file and try to write again 
# then all the earlier content will be wiped
f.close()

f = open('sample2.txt','a')
f.write('I am appending\n')
f.close()