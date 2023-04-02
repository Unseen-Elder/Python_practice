
def table(num):
    i=1
    while(i<=10):
        print( num + " X " + str(i) +" =",(int(num))*i)
        i=i+1

num=input("Entre the number you want table of : ")

table(num)