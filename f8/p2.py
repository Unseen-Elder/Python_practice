def greet(Name="Stranger"):
    print("Good Day "+Name)
    

name = (input("Entre your name : "))
greet(name)

greet() # default parameter value in this function is Stranger, Stranger is used when no argument is passed