def temp(celcius):
    farhenite = celcius*(9/5) +32
    farhenite = round(farhenite,2)
    return farhenite

celcius=int(input("Entre the temperature in Celcius\n"))

print("The temp in Farhenite is",temp(celcius))