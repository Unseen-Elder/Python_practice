f1 = input("Entre your name : ")
l1 = input("Entre Your facvourite language : ")

f2 = input("Entre your name : ")
l2 = input("Entre Your facvourite language : ")

f3 = input("Entre your name : ")
l3 = input("Entre Your facvourite language : ")

f4 = input("Entre your name : ")
l4 = input("Entre Your facvourite language : ")

dict ={}
dict2= {
    f1 : l1,
    f2 : l2,
    f3 : l3,
    f4 : l4,
}

dict.update(dict2)
print(dict)

#if i write same keys their values will be overwritten and only latest value will be stored