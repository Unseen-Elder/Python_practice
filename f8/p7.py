def summ(num):
    if(num == 0):
        return 0
    elif(num == 1):
        return 1
    else:
        return num + summ(num-1)

num= int(input("Entre the number\n"))

print(f"The sum of first {num} natural numbers is {summ(num)}")
