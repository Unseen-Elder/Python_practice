# Working of is and is not
# only works when a is None , because is operator is used to check if both are pointing to same object.
# == and != is used to check the values

a=None
if(a is None):
    print("Yes")
else:
    print("No")

# Working of in operator
# Returns true or false based on object present in a list or dict or tuple or set

tup= (1,5,6,3,2,1,4,5)
list = [23,34,23,53,23]
set = {1,3,4,6,2,5,3}
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
print(5 in tup)
print(2 in list)
print(4 in set)
print("Vipul" in Dict)