num1= int(input("Entre first Number : "))
num2= int(input("Entre second Number : "))
num3= int(input("Entre third Number : "))
num4= int(input("Entre fourth Number : "))

if(num1>=num2):
    f1=num1
else:
    f1=num2

if(num3>=num4):
    f2=num3
else:
    f2=num4

if(f1>=f2):
    print(str(f1)," is greatest")
else:
    print(str(f2)," is greatest")