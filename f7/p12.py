num= int(input("Entre your number : "))

count=0

for i in range(1,num):
    if(num%i==0):
        count=count+1

if(count<=1):
    print("Prime")
else:
    print("Not prime")