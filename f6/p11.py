marks = int(input("Entre your marks\n"))

if(marks<=100 and marks>=90):
    grade="A"
elif(marks<90 and marks>=80):
    grade="B"
elif(marks<80 and marks>=70):
    grade="C"
elif(marks<70 and marks>=60):
    grade="D"
elif(marks<60 and marks>=50):
    grade="Pass"
elif(marks<50 and marks>0):
    grade = "Fail" 
elif(marks<0 or marks >100):
    print("Entre valid marks")

if(marks>=60 and marks<=100):
    print("Your Grade is "+grade)
elif(marks<60 and marks>=50):
    print("You have Passed with P grade")
elif(marks<0 or marks >100):
    pass
else:
    print("You Failed")