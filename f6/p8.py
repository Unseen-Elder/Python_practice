text = input("Entre your text : ")

a =False

if("Make Money Fast" in text):a=True
elif("Enlarge Your Penis" in text):a=True
elif("Buy Now" in text):a=True
elif("Subscribe This" in text):a=True
elif("Click This" in text):a=True

if(a == True):
    print("Its a spam")
else:
    print("its not a spam")