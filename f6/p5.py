num1= input("Entre first Number : ")
num2= input("Entre second Number : ")
num3= input("Entre third Number : ")
num4= input("Entre fourth Number : ")

num1= (int)(num1)
num2= (int)(num2)
num3= (int)(num3)
num4= (int)(num4)

greatest=0

if(num1>num2 and num1>num3 and num1>num4):
    greatest=num1
elif(num2>num1 and num2>num3 and num2>num4):
    greatest=num2
elif(num3>num1 and num3>num2 and num3>num4):
    greatest=num3
elif(num4>num1 and num4>num3 and num4>num3):
    greatest=num4


print("The greatest number is : ",str(greatest))