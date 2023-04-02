def rmv(lst,str):
    a=len(lst)
    for i in range(a):
        lst[i]=lst[i].strip()
    
    lst.remove(str)

num=int(input("Entre the number of elements in string\n"))
lst=[]
for i in range(num):
    text=input("Entre the element of string\n")
    lst.append(text)

remov = input("Entre the element you want to remove from list\n")

rmv(lst,remov)

print(lst)