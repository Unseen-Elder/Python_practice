def fact(num):
    if(num==1 or num ==0):
        return 1
    else:
        return num*fact(num-1)

num= int(input("Entre the number you want factorial of\n"))

a=fact(num)

print(f"The factorial of {num} is {a}")