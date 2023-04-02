a= input("entre a number :") # input always take input in form of string
print("type of a before typecasting ",type(a))

# b = a+5, this will show error because a is a string, we need to typecast a into an integer

a=int(a)
print("type of a after typecasting", type(a))

b=a+5
print(b)

c=input("entre a name :")
#if c is a string of characters then we cannot typecast character string into integer
# c = int(c) will show error