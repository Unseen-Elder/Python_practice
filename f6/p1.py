a=40

if(a>3):
    print("Indentation has huge role to play in python.")
    print("The value of a is greater than 3") #indentation is used to tell that next line is in if.
elif(a<3):
    print("The Value of a is less than 3")
else :
    print("The value of a is equal to 3")

b=50

if(b>3):
    print("The value of b is greater than 3")
elif(b>9):
    print("The Value of b is less than 9") # this will not be printed because "if-elif" ladder is broken at first step
else :
    print("The value of b is less than or equal to 3")

c=30

if(c>20):
    print("The value of c is greater than 20")

if(c>10):
    print("The value of c is greater than 10")

if(c>40):
    print("The value of c is greater than 40")