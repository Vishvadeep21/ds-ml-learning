capitals = {"USA": "Washington D.C.",
                    "India": "New Delhi",
                    "China": "Beijing",
                    "Russia": "Moscow"}

print(capitals)
print(capitals.get("Japan"))
# returns the values of the key given within the function

if capitals.get("Russia"):
  print("That capital exists")
else:
  print("That capital doesn't exist")

capitals.update({"Germany": "Berlin"})  
capitals.update({"USA": "Detroit"})
# adds the new value to the existing dictionaries

capitals.pop("China")
# removes the items from dictionary
capitals.popitem()
capitals.clear()
# deletes whole elements and make dictionary empty

keys = capitals.keys()
# Prints all keys in a list(which means keys and values are stored in a list)
for key in capitals.keys():
    print(key)

values = capitals.values()
# prints all values of a dictionary in a list
for value in capitals.values():
    print(value)

items = capitals.items()

# prints the items of a dictionary
for key, value in capitals.items():
    print(f"{key}: {value}")
