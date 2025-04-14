# Set - Collection of the unordered items
# Each element must be unique and immutable
# Examples - nums = {1,2,3,4}
# Example 2 - set2 = {1,2,2,2}, repeated elements stored only once so it resolved to {1,2}
# null_set = set() #empty set syntax

collection = {1, 2, 3, 4}
collection2 = {1, 4, 5, 6}
print(collection)
print(type(collection))
print(len(collection))

# Collection Methods
collection.add(12)  # adds an element
print(collection)
collection.remove(3)  # removes an element
print(collection)
collection.pop()  # removes a random value
print(collection)
collection.clear()  # empties the set
print(collection)

collection = {1, 2, 3, 4}
collection2 = {1, 4, 5, 6}
# Combines all the values of both the sets and return a set
print(collection.union(collection2))
# combines all the common values and returns a set
print(collection.intersection(collection2))
