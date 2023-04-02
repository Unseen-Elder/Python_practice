m1=float(input("Entre marks in 1st subject : "))
m2=float(input("Entre marks in 2nd subject : "))
m3=float(input("Entre marks in 3rd subject : "))

avg = float((m1+m2+m3)/3)
avg = round(avg,2)

if(m1>33 and m2>33 and m3>33 and avg>40):
    print("pass with "+str(avg) + "%")
else: 
    print("fail")