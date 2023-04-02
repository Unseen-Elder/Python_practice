letter = '''Dear name
You are Selected !!
date'''

name = input("Entre Your name\n")
date = input("Entre Date in dd/mm/yyyy format \n")

letter = letter.replace("name",name)
letter = letter.replace("date",date)

print(letter)