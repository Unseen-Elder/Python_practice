num = int(input("Entre your number : "))

for i in range(1,num+1):
    for j in range(1,i+1):
        print("*",end ='') # "end ='' " will print the next result in same line .
    print("\n")