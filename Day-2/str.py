str1 = "This is a string. \n We are creating it in Python."
print(str1)

# Concatenation
print("Hello"+"world")  # Should give Helloworld as output

# Length of a  - len()
print(len("Hello"))  # Gives the length of the string - Here it will be 5

# indexing - may be accesed using str[i]
print(str1[len(str1) - 1])

# Slicing - Accesing part of the string - Syntax : str[ starting_index : ending_index ] #ending index is not included
str = "Apna College"
print(str[1: 4])
print(str[: 4])  # Same as str[0 : 4]
print(str[1:])  # same as str[1 : len(str)]
# negative indices referring to the counting in the negative direction
print(str[-3: -1])

# String Functions
str = "i am a old world coder."
print(str.endswith("er."))  # returns true if the string ends with the substr
print(str.capitalize())  # capitalise the first character of the string
print(str.replace("old", "new"))  # replaces all the occurences of old with new
print(str.find("world"))  # returns the 1st index of 1st occurence
print(str.count("am"))  # counts the occurence of substr in the string
