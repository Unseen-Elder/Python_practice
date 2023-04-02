a=input("Entre your age : ")
a=(int)(a)

b=input("Entre your Salary : ")
b=(int)(b)

c=input("Entre The Value of Your Asset :")
c=(int)(c)

if(a>=18 and a<60):
    print("Working Age")
else:
    print("Cannot work")

if(b>50000 or c>3000000):
    print("Rich")
elif(not(b>50000 or c>3000000)): #i could have used else but just to show not operator i have used this
    print("Not rich")

