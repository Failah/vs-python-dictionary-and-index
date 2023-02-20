# index operator [] gives access to a sequence's elements (strings, lists, tuples)

name = "valerio Failah"

if name[0].islower():
    name = name.capitalize()

print(name)
print()

# first_name = name[0:7].upper()
first_name = name[:7].upper()  # shortcut when index starts from 0 (or the last, see below)
last_name = name[8:].lower()
print(first_name, last_name)
print()

# negative indexing is used to start iterating from the last element to the first
last_char = name[13:7:-1]
print(last_char)