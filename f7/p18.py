num = int(input("Entre your number : "))

print("* "*num)

for i in range(1, num-1):
    print("* " + "  "*(num-2) +"*")

print("* "*num)