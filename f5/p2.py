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

print(Dict.keys())
print(type(Dict.keys()))

#we can typecast dict_keys into list

Typecasted_keys = (list)(Dict.keys())
print(Typecasted_keys)
print(type(Typecasted_keys))

print(Dict.values())
print(type(Dict.values()))

Typecasted_values = (list)(Dict.values())
print(Typecasted_values)
print(type(Typecasted_values))

print(Dict.items()) # gives items in form of list of tuples.
print(type(Dict.items()))

Typecasted_items = (list)(Dict.items())
print(Typecasted_items)
print(type(Typecasted_items))