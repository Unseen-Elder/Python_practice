greeting = "Good Morning, "
name = "Vipul"

print(greeting + name) # concatinating two strings

print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])

# name[3]=k , this doesnot work 


# String slicing
print(name[0:3]) # name[3] wont be included
print(name[1:4]) # name[1] will be included
print(name[:3])  # it will start from minimum indices
print(name[2:])  # print upto last indices

# negative indices of string, used when we dont know size of string

print(name[-1])
print(name[-2])
print(name[-3])
print(name[-4])
print(name[-5])

print(name[-3:-1])

# slicing with skip

print(greeting[0:13:3]) # it will print string by skipping every 3 characters
print(greeting[0:13:2]) # it will print string by skipping every 2 characters

#string functions

story = '''twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky.
Twinkle, twinkle, little star,
How I wonder what you are!'''

print(len(story))
print(story.startswith("twinkle"))
print(story.endswith("wonder what you are!"))
print(story.endswith("Twinkle, twinkle"))

print(story.count("winkle"))
print(story.count("s"))
print(story.count("z"))
print(story.count("a"))


print(story.capitalize()) # make the first word capital in string

print(story.find("twinkle")) # this will return -1 if word is not in the string ,or will return the index of first occurance of the word
print(story.find("wonder"))
print(story.find("vipul"))

print(story.replace("twinkle","binkle")) # all occurances will be replaced
print(story.replace("binkle", "twinkle"))

#Escape sequences

essay="\tA cow is a domestic animal.\n\tCows are one of the most innocent animals who are very harmless."
print(essay)


#to print backslash or single quote

string= "\\ ,\'"

print(string)