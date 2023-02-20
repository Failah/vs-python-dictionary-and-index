# dictionary is a changeable unordered collection of unique key:value pairs

capitals = {"USA": "Washington DC",
                "Italia": "Roma",
            "Francia": "Parigi",
            "Spagna": "Madrid"}

# we have no indexes, we use keys to access values

print(capitals["Italia"])  # this works

print(capitals.get("Russia"))  # a key not present = None
print()

print(capitals.keys())
print()

print(capitals.values())
print()

print(capitals.items())
print()

for key, value in capitals.items():
    print(key, value)
print()

# the update method modifies the items in the dictionary
capitals.update({"Russia": "Mosca"})  # modifies an existing key value
print(capitals.items())
print()

capitals.update({"Italia": "Torino"})
print(capitals.items())
print()

# the pop method removes a pair
capitals.pop("Italia")
print(capitals.items())
print()

# the clear method clears the entire dictionary
capitals.clear()
print("Empty capital list: ", capitals)