# Dictionary is unordered
# It is mutable
# it cannot contain duplicate keys

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

print(Dict['Vipul'])
print(Dict['Toothpick'])
print(Dict['Toothpick'][4])
print(Dict['Pen'])
print(Dict['String'])
print(Dict['list'])
print(Dict['list'][1])
print(Dict['tuple'])
print(Dict['Another_Dict'])
print(Dict['Another_Dict']['Cricket'])
print(Dict['Another_Dict']['pingpong'])
print(Dict[1])
print(Dict[2])


