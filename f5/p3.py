Dict = {
    "Vipul": "An Engineer",

    "Toothpick": "To clean teeth",

    "Pen" : "To write notes",

    "String" : ['''Twinkle, twinkle, little star,
                   How I wonder what you are!
                   Up above the world so high,
                   Like a diamond in the sky.
                   Twinkle, twinkle, little star,
                   How I wonder what you are!'''],

    "list" : ["vipul","prateek","shubham"],

    "tuple" : ("sattu","vaibhav","gulshan"),

    "Another_Dict" : {
        "pingpong" : "A game",
        "Cricket" : "Also a game"
    },

    1 : 65,
    2 : "a number"
}
Updt_Dict = {
    "vipul" : "Human",
    "Tommy" : "Dog",
    "Moti" : "Bull",
    "String" : "hello"
}
print(Dict.items())

Dict.update(Updt_Dict)# updates the dictionary by adding key : value pairs from new dictionary.
# Also overwrites the existing key value player, if it is also present in new dictionary.

print(Dict.items())

print(Dict.get("vipul"))
print(Dict.get("vikas"))

# if we use print(Dict['vikas']) then we will get error,but print(Dict.get("vikas")) will return None