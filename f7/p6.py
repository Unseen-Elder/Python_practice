for j in range(2,20,2):
    if(j==8):
        continue # it is used to skip a particular value in loop. nothing below continue is executed in loop
    print(j)

print("\n")

#printing even numbers using continue
for j in range(1,20):
    if(j%2!=0):
        continue # it is used to skip a particular value in loop.
    print(j)