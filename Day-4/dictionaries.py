# Dictionaries - are used to store data values in key:value pair
# -unordered, mutable , don't allow duplicate keys
# example : dict = {
# "name" : "Prince",
# "cgpa" : 9.6,
# "marks" : [97,98,80]}
info = {
    "key": "value",
    "name": "Apna College",
    "age": 35,
    "marks": 94.4,
    "subjects": ["maths", "physics"],
    "topics": ("dict", "set"),
}
print(info)
print(type(info))
print(info["name"])  # Accessing the values using key

# nestedDIctionaries - Dictionary in a dictionary
student = {
    "name": "Prince",
    "score": {
        "maths": 98,
        "chem": 90,
        "physics": 92,
    },
}

# Dictionaries Methods
# returns all the keys - may be typecasted to list using - list(info.keys())
print(info.keys())
print(info.values())  # returns all the values
print(info.items())  # returns all (key, value) pairs as tuples
print(info.get(35))  # returns the key according to the value
# inserts the specified item to the dictionary
info.update({"city": "Delhi"})
print(info)
