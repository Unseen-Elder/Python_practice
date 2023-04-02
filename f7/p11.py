l1=["Harry","Sohan","Sachin","Rahul"]

for name in l1: #here "name" is the the name of variable, which will move start to end of the list
    if(name.startswith("S")): # .startswith is a method to check first letter of a string
        print("Good Morning "+name)
    else:
        pass