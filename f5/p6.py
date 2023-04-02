#adding values to a set

a=set()

a.add(3)
print(a)

a.add('''"Vipul"''')
print(a)

#if we add same element mutiple time in a set , it will remain unchanged
#cannot add list to set
#can add tuple to a list
#cannot add dictionary to list

tup=(9,3,2) # here 3 in this tuple will not be considered duplicate element

a.add(tup)

print(a)

# we cannot change items in set

print(len(a)) #prints the length of set

a.remove('''"Vipul"''')
# a.remove(12) will throw an error because it is not present in set

print(a)

print(a.pop()) #remove an arbitary element from set and returns it value
print(a)

a.clear() #will clear all elements of set
print(a)