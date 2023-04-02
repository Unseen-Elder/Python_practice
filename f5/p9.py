dict = {
    "Baccha" : "Kid",
    "Mota" : "Fat",
    "Patla" : "Lean / Slim"
}
print("Avalianle Hindi words : ", dict.keys())
a=input("Entre your Hindi word : ")
print("English Meaning : ",dict.get(a))