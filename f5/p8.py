from operator import index


dict = {
    "Baccha" : "Kid",
    "Mota" : "Fat",
    "Patla" : "Lean / Slim"
}

print(dict["Baccha"])
print(dict["Mota"])
print(dict["Patla"])

print(dict.get("Baccha"))
print(dict.get("Mota"))
print(dict.get("Patla"))

print(dict.keys())
print(dict.values())
print(dict,index)