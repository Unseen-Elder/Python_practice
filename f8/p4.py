def greatest(num1,num2,num3):
    if(num1>=num2 and num1>=num3):
        return num1
    if(num2>=num1 and num2>=num3):
        return num2
    if(num3>=num2 and num3>=num1):
        return num3

num1=int(input("Entre 1st Number : "))
num2=int(input("Entre 2nd Number : "))
num3=int(input("Entre 3rd Number : "))

print("The greatest number is",greatest(num1,num2,num3))