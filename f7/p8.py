table=input("Entre the number you want table of : ")

for i in range(1,11):
    print( table + " X " + str(i) +" =",(int(table))*i)

print("\n")

table= int(table)
for i in range(1,11):
    print(f"{table} X {i} = {table*i}") # will do the same work as above
